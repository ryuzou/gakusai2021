import base64
import json
import math
import threading
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
from multiprocessing import Process
from multiprocessing import Pipe
import time
import cv2
import numpy as np
import pygame
from pygame import locals

from concurrent.futures import ThreadPoolExecutor


def update_controller(joystick_data):
    gameDict = {"joystick": {"radius": 0, "stick_degree": 0}, "shot_button": 0, "reload_button": 0, "left": 0,
                "right": 0}

    # ジョイスティックの初期化
    pygame.joystick.init()
    try:
        # ジョイスティックインスタンスの生成
        joystick = pygame.joystick.Joystick(0)
        joystick.init()
        print('ジョイスティックの名前:', joystick.get_name())
        print('ボタン数 :', joystick.get_numbuttons())
    except pygame.error:
        print('ジョイスティックが接続されていません')

    # pygameの初期化
    pygame.init()

    global gameJson

    joystick_radius = 0
    joystick_stick_degree = 0
    shot_button = 0
    left = 0
    right = 0
    reload_button = 0

    x = 0
    y = 0

    while True:
        for e in pygame.event.get():
            if e.type == pygame.locals.JOYAXISMOTION:
                y = joystick.get_axis(0)
                x = -(joystick.get_axis(1))
                joystick_radius = int((math.sqrt(x ** 2 + y ** 2) / math.sqrt(2)) * 100)
                rad = math.atan2(y, x)
                if y < 0:
                    joystick_stick_degree = int(math.degrees(rad) + 360)
                else:
                    joystick_stick_degree = int(math.degrees(rad))
                # print(f"θ={joystick_stick_degree},r={joystick_radius},x={x},y={y}")
            elif e.type == pygame.locals.JOYBUTTONDOWN:
                if e.button == 1:
                    shot_button = 1
                elif e.button == 0:
                    reload_button = 1
                elif e.button == 4:
                    left = 1
                elif e.button == 5:
                    right = 1
            elif e.type == pygame.locals.JOYBUTTONUP:
                if e.button == 1:
                    shot_button = 0
                elif e.button == 0:
                    reload_button = 0
                elif e.button == 4:
                    left = 0
                elif e.button == 5:
                    right = 0

            # JSON書き込み
            (gameDict["joystick"])["radius"] = joystick_radius
            (gameDict["joystick"])["stick_degree"] = joystick_stick_degree
            gameDict["reload_button"] = reload_button
            gameDict["shot_button"] = shot_button
            gameDict["left"] = left
            gameDict["right"] = right
            joystick_data.updateData(gameDict)

def imageGetter():

    baseImg = np.zeros((480, 640, 3)).astype('int')
    baseImg += [0, 0, 255][::-1]  # RGBで青指定

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 5]
    result, encimg = cv2.imencode('.jpg', baseImg, encode_param)
    if False == result:
        print('could not encode image!')
        exit()

    decimg = cv2.imdecode(encimg, cv2.IMREAD_COLOR)
    baseImg = decimg

    PORT_UDP = 8092

    socket_udp = socket(AF_INET, SOCK_DGRAM)
    socket_udp.bind(("0.0.0.0", PORT_UDP))

    buff = 1034 * 64

    imagePartDict = {}

    initialised_flag = False

    while True:
        data, _ = socket_udp.recvfrom(buff)
        data = data.decode()

        header = data.split("&")[0]
        x_cod = int(header.split("_")[0])
        y_cod = int(header.split("_")[1])

        if initialised_flag == False:
            x_len = int(header.split("_")[2])
            y_len = int(header.split("_")[3])
            initialised_flag = True


        timestamp = int(header.split("_")[4])
        xycodOD = str(x_cod) + str(y_cod)

        runFlag = True
        if xycodOD in imagePartDict:
            if imagePartDict[xycodOD] >= timestamp:
                runFlag = False
            else:
                imagePartDict[xycodOD] = timestamp
        else:
            imagePartDict[xycodOD] = timestamp

        #print(data)

        if runFlag:
            img_data = base64.b64decode(data.split("&")[1])
            nparr = np.frombuffer(img_data, np.uint8)
            img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            baseImg[y_cod:(y_cod + y_len), x_cod:(x_cod + x_len)] = img_decode
            cv2.imshow("img", baseImg)
        if cv2.waitKey(1) != -1:
            break


def json_sender(joystick_data):
    IPADDR = "192.168.0.3"
    PORT_TCP = 8000
    socket_tcp = socket(AF_INET, SOCK_STREAM)
    socket_tcp.connect((IPADDR, PORT_TCP))
    gameDict = {"joystick": {"radius": 0, "stick_degree": 0}, "shot_button": 0, "reload_button": 0, "left": 0,
                "right": 0}
    baseGameJson = joystick_data.getData()
    global gameJson
    while True:
        socket_tcp.send(((baseGameJson + '\n').encode("utf-8")))
        print(baseGameJson)
        baseGameJson = joystick_data.getData()

class JoystickData:
    lock = threading.Lock()
    gameJson = json.dumps({"joystick": {"radius": 0, "stick_degree": 0}, "shot_button": 0, "reload_button": 0, "left": 0, "right": 0})

    def updateData(self, dataDict):
        dataJson = json.dumps(dataDict)
        with self.lock:
            self.gameJson = dataJson

    def getData(self):
        with self.lock:
            ret = self.gameJson
        return ret

def main():
    joystick_data = JoystickData()
    with ThreadPoolExecutor() as executor:
        thread1 = executor.submit(update_controller, joystick_data)
        thread2 = executor.submit(json_sender, joystick_data)
        thread3 = executor.submit(imageGetter)

        features = [thread1, thread2, thread3]

if __name__ == '__main__':
    main()