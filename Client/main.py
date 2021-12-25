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
    gameDict = {"joystick": {"radius": 0, "stick_degree": 0}}

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

            # JSON書き込み
            (gameDict["joystick"])["radius"] = joystick_radius
            (gameDict["joystick"])["stick_degree"] = joystick_stick_degree
            joystick_data.updateData(gameDict)

def json_sender(joystick_data):
    IPADDR = "192.168.0.7"
    PORT_TCP = 8000
    socket_tcp = socket(AF_INET, SOCK_STREAM)
    socket_tcp.connect((IPADDR, PORT_TCP))
    gameDict = {"joystick": {"radius": 0, "stick_degree": 0}}
    baseGameJson = joystick_data.getData()
    global gameJson
    while True:
        socket_tcp.send(((str(str(baseGameJson['joystick']['radius']) + ',' + str(baseGameJson['joystick']['stick_degree'])) + '\n').encode("utf-8")))
        baseGameJson = joystick_data.getData()

class JoystickData:
    lock = threading.Lock()
    gameJson = {"joystick": {"radius": 0, "stick_degree": 0}}

    def updateData(self, dataDict):
        dataJson = dataDict
        with self.lock:
            self.gameJson = dataDict

    def getData(self):
        with self.lock:
            ret = self.gameJson
        return ret

def main():
    joystick_data = JoystickData()
    with ThreadPoolExecutor() as executor:
        thread1 = executor.submit(update_controller, joystick_data)
        thread2 = executor.submit(json_sender, joystick_data)

        features = [thread1, thread2]

if __name__ == '__main__':
    main()