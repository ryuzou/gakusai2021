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


def main():
    IPADDR = "192.168.0.4"
    PORT_TCP = 8000
    socket_tcp = socket(AF_INET, SOCK_STREAM)
    socket_tcp.connect((IPADDR, PORT_TCP))

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
                print(f"θ={joystick_stick_degree},r={joystick_radius},x={x},y={y}")
                socket_tcp.send(((str(joystick_radius) + ',' + str(joystick_stick_degree)) + '\n').encode("utf-8"))



if __name__ == '__main__':
    main()