import base64
import json
import math
import threading
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
import time
import cv2
import numpy as np
import pygame
from pygame import locals

gameJson = None


def update_controller():
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
            lock.acquire()
            gameJson = json.dumps(gameDict)
            lock.release()
            # print(gameJson)


def status_observer():
    baseImg = np.zeros((960, 1280, 3)).astype('int')
    baseImg += [0, 0, 255][::-1]  # RGBで青指定

    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 5]
    result, encimg = cv2.imencode('.jpg', baseImg, encode_param)
    if False == result:
        print('could not encode image!')
        exit()

    global gameJson

    lock.acquire()
    local_gamejson = gameJson
    lock.release()

    decimg = cv2.imdecode(encimg, cv2.IMREAD_COLOR)
    baseImg = decimg

    IPADDR = "192.168.0.8"
    PORT_TCP = 8000
    PORT_UDP = 8092

    socket_tcp = socket(AF_INET, SOCK_STREAM)
    socket_tcp.connect((IPADDR, PORT_TCP))

    socket_udp = socket(AF_INET, SOCK_DGRAM)
    socket_udp.bind(("0.0.0.0", PORT_UDP))

    buff = 1034 * 64

    while True:
        lock.acquire()
        local_gamejson = gameJson
        lock.release()
        print(local_gamejson)
        socket_tcp.send(((local_gamejson + '\n').encode("utf-8")))
        time.sleep(0.1)
        """data = bytes()
        data, _ = socket_udp.recvfrom(buff)
        data = data.decode()

        header = data.split("&")[0]
        x_cod = int(header.split("_")[0])
        y_cod = int(header.split("_")[1])

        x_len = int(header.split("_")[2])
        y_len = int(header.split("_")[3])

        timestamp = int(header.split("_")[4])

        print(data)

        img_data = base64.b64decode(data.split("&")[1])
        nparr = np.frombuffer(img_data, np.uint8)
        img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        baseImg[y_cod:(y_cod + y_len), x_cod:(x_cod + x_len)] = img_decode
        cv2.imshow("img", baseImg)
        if cv2.waitKey(1) != -1:
            break"""


lock = threading.Lock()
thread_1 = threading.Thread(target=update_controller)
thread_2 = threading.Thread(target=status_observer)
thread_1.start()
thread_2.start()