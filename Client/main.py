import base64
from socket import socket, AF_INET, SOCK_DGRAM, SOCK_STREAM
import cv2
import numpy as np
import json


gameDict = {"joystick": {"r": 0, "sita": 0}, "shoot": 0, "LR": 0}
gameJson = json.dumps(gameDict)
print(gameJson)

import pygame
from pygame.locals import *

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

# 画面の生成
screen = pygame.display.set_mode((320, 320))

# ループ
active = True
while active:
   for e in pygame.event.get():
       if e.type == pygame.locals.JOYAXISMOTION:
           print('十時キー:', joystick.get_axis(0), joystick.get_axis(1))
       elif e.type == pygame.locals.JOYBUTTONDOWN:
           print('ボタン'+str(e.button)+'を押した')
       elif e.type == pygame.locals.JOYBUTTONUP:
           print('ボタン'+str(e.button)+'を離した')

baseImg = np.zeros((960, 1280, 3)).astype('int')
baseImg += [0, 0, 255][::-1]  # RGBで青指定

encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 5]
result, encimg = cv2.imencode('.jpg', baseImg, encode_param)
if False == result:
    print('could not encode image!')
    exit()

decimg = cv2.imdecode(encimg, cv2.IMREAD_COLOR)
baseImg = decimg


IPADDR = "192.168.0.6"
PORT_TCP = 8000
PORT_UDP = 8092

socket_tcp = socket(AF_INET, SOCK_STREAM)
socket_tcp.connect((IPADDR, PORT_TCP))
socket_tcp.send(gameJson.encode("utf-8"))

socket_udp = socket(AF_INET, SOCK_DGRAM)
socket_udp.bind(("0.0.0.0", PORT_UDP))

buff = 1034 * 64

while True:
    socket_tcp.send(gameJson.encode("utf-8"))

    data = bytes()
    data, _ = socket_udp.recvfrom(buff)
    data = data.decode()

    header = data.split("&")[0]
    x_cod = int(header.split("_")[0])
    y_cod = int(header.split("_")[1])

    x_len = int(header.split("_")[2])
    y_len = int(header.split("_")[3])
    print(data)

    img_data = base64.b64decode(data.split("&")[1])
    nparr = np.frombuffer(img_data, np.uint8)
    img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    baseImg[y_cod:(y_cod + y_len), x_cod:(x_cod + x_len)] = img_decode
    cv2.imshow("img", baseImg)
    if cv2.waitKey(1) != -1:
        break
"""

data = b'0_0_160_120&/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/wAALCAB4AKABAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/APQNLgvGjeWKy+zuE+W1c7tgzjr9eatMjttS9t2UFDvLYVj+XQ1DcTSQsEMbkoQAWTjp0qsLiQzSTl5EAQ7QQOB6VPazt1ETIHPJfuPalSXy0eykY7EJOX4x/Ump0uEeCSVJeVUF1ZdxPHAGOBjvmmy3CzQRtNcKN0WSduBUcl1CIDGAWVCAoY4yKBI4KuJBEBGAoHJpYnt5EWERHIP7sl+M565ptxJeouWcRPITuZVHzY6HnjHWq5YyxJJ5AfbIGEZbac9zj0qC6mEE7pJAUM4Kku+dgPp2zUZkjhk2RuxCjGNuCCO/Pak3IYmSUhsA4VOdwp8FyrsGVWIQZJZuoFIhYx7JYwDkk56gH/61RXca22GjkVschQTkD+v/ANaptOuYUkjUxeaZE+XJxtH0FakB05NmyVVLqWKqxJT0qaOSF2aWMOzun3mXkN0Bx0qeG4uIS7LZSQuo2lpGBI45JB/zzVJ7YNGIYSo7sWblvYeopiSgZWdXYZCIF5wO5pk0cE8rpJKAqOR5ZOG6VAUFo7ralRujwELYGfp3zSfafNXyd5UscdMjFBlMRJ8wjYmACMhmz0I9MVELyOSQvJat5ajgM2Ru9OP88VJHdCGQEruy2FQDnJqRniklIEWMAYQtuHvn09KhvL6FVYzj75ypKkkjPt0qtFNDcq4WMtnG+OWNsKo9Mj9aCJDKCn7wFMJuP3TnnFQuXuELKwODglRgD6etLlrciIFcMCQGXOD2H1qSS4kbYRIFmfB2EY2+1SPIJVRAOqEjA5/+sDVR7iJJQYR5YVcMP4ie9a1urxoy2jxlCQBsTbuGfTtUxmFyWjmmkURkbVHJHPXNPfVne4ZoYjJubqz7mbtknualS5sbhFVpEQqMMV5IPv7063adSgtpVwhLYXHzH3HrRcRWbAzXVmRICCMDrnqTURsryWZ54Y1cMmcKo4x3qq1pNE6XE0ZUd9vp7imeTE8wYOEZgcgr+VMuVuIkxEn+qXEjKcAZ559u9Rq0ZYAxAYcbdudx4pxa6TzATtcqDGr8kgfzpN4X99PGzZUfvAOB9KSfU9UvEiEt9M6BSFZpc7T24PSoTFLKCbpVi8sj7r5GaSOzfzzEgMisnAJxn39qhIMKblVxl8FSwILDoT6/SgG5diJ5VeQc+YDwfXP0qRXRJlj3bl24RicFc+o9Paor2Fgy5AQ87CrZ3GtOwUQweQ45DZVyoUbfQDtUsrRSTLJMxDhSCeu7396V4ysC7lxGykpKCM8e1QpNHHIjLK374qXUrncPx7VOty7SObfYoUEpCWxkexHephqLZ2y2ySRgj70pzH659atM6eaI40KP5hy27Bxj2/houLW9jt/NkhWQHkjfnP5dKrzQwzSG5VSCFDeW54C9wPxqle6RIMs0p8lwWcAZ57CoUEkZeIRbSUURlm+4OhHue/4USRMqKwOWj4Eu7rnvn2qv806qPOQZOULHHT+VMuZolmZ1ZcjaWi6Z9T+HpUObdQ11Gy/vZP3asSTn19qkuJvPgjaVAJMZQnpj3xSosEbE7gwbOSeD06Ypt1YXOl3UdrcqMyRK6L97ap+709etRSRz7XljK70XJ3+1QrOWi8sgSZOMljwfb19K2xFJDcC3MoVUIZExz0559OtTIjOrRxAOONzSEYjU+lV9Re2iJAiUquBuXOAe5HtUUTvcmIyF8xHGH7A9h6CpraCR5WZrZhGpO7MgBz6CrMDEyGaIoxUbSkgwTxzio4QkCKP3pOCWITO3vj6UsV/eWql4JSsjkfMTwAe5q0mq2r4N9Cr7VIEqqRg9xx1FBFtIxmsdZKEEEwuPmPuKULNMjyzxPKGPEoTcT7cUyKzh1GBf7MO/YwBQjHzdvc/SqOpW/kXIW4gjb5zww+UEdjj+lUhGsm4S7QGGUfbgE1E8JQEyM5XPyKoHP0NRFZEIZQ/GQ8e3qfT/AOvU3nTRSN85iHlDLoN31xUDXFkzyCzuLkADkHAO30Pp+FKGRlJeQsmQSd3INRTBJOHl2uSMsq8BfQj29a1bSHMQSfeELECYHkj0qzboqSLHHFuQqFAPAXk/MaUpHIHExcoCcR5GQexB9KZvkiQHymIIwkrfzxQsNoFQ4eVm5Zycqv8A9ept0RLzRyF1jXBkbAy3YYqKXfKV33DDPMmTg/8A1hTLj7SsLwGVURRvKtyHx70R3KRzK6JgNGGcNwvTkkelNS4Ubp1tgnVTnkKex+lWdM1vVtJmW90y5ZG7g4x/k1Yutf024VZLyNbZmblo1wQT3qyFlyItLZJlVMjzgPm+gPeqU1raEbbi0lt5WzvZiMA+q+hqne6dKVeW22Ou1Snln5Qe7VnzZ814nBUqAHcNkMfaoVRzLJGYiyiL5g78YNJKIYH2mFFyNxIOaZ5zTSh44lAY7ULLwG+noKR5btmAWSMlflYdm9xXRS3UFyGxbr+9AYuFKgAdcL27/nTXdVlVgW2YIRj/ABU4LbsWjEZDgHaw/wAO2KiS6CSLFIwVsYRMZxnqfrTvMUJ5a/OQoDhvlTA9cdaZFM6FvMKMGGWjCYHsf/r083SooUQeYpQknbyufeopvLRkW5lI3HDZTHGODxSeZMYfIeRDuQZYjpzTZLifPmWwDbRtZWOdxP8AOkhlnSH5/LbflcAnI9/Y08TFl/dReYzRkYYDIHf6UjTRJLn+1NxRVKw4xsyKtReJLpIRFKtrcL/CJEOR7Z7UfbNGuCpa5ks95+VUGULU+Vba0eSdNlwjKE3Ffm3eo+n5VSl0W3uZH8vUmgnUjZIVziqk2mzWfzsZJ0yd8hjwQf73vVS7CrELZZFwGOCM9fWmBBHKzNCGVYwfLzweMcV0QhVZNztPJGufKE64kA9D702BLyIG3kjIDEuiuM4XPQntT9rph+CGXIxycfWolEErozSOwJwARjH1Pf8ACnSTQwsQ8alMcADKmnfZgSjyJIuwAlj0YHnA7VDIySk/ZpGVeW6fKB6AU1lk8oIGC7uTnsvaq8sphXzS4eIMBJnqp7E+1Oia4zL5rhdjcMBhiT6H6Uj5LGZlAjjzkscMD64701CQi3ao77gdoPBHuf8ACkITzhK1sqEgB3Y88VGd0Z88RScZZwccD1Hv7VWna6vLYlHzAhzn1OelW4NRnSVZolYlVC9c/L2BFWn8STyysbi2icD702MMo9OOtSreWUsUksOrTKyrujhC4Vz6e1U7loZ0IurTBzzhfmP4eoqq2noX2x4YBflBOK6SDfcILqO4ZolOC0+Syt3B9OKtiRLljHhHUIVUqTk/ge3+NUmsojG6TxurMR8rPjj0A/KoL2BJlkgiTcqyAorHlRgA/T3qKGUW8Tu9sxZehccADpj1NTSLdTPAJJX2qrSIpPr/AEqAyzS4iadTuPVz0p6NJLCIlEZVSQxVsn6YqKdIppyMKo2HbuXBz02n61WBtQ7ShSGK4x2Vc/dB/qadAjSExoSTIOGbggde9CrcMjszq+B+7IHU+lNYTO204YEZ2sfun0PqKh+0PcyBosll4xt4xn3qExRxMYmlV9pLMi9T9faiPERdo5lO07sJ8ufb0qP/AEmOYkugKtnzF4BzzigMZA7/AGhVBfBUYBP51Mt15EpYSMseDgsPvH+tLBqKXU2ZAcqpJZI8kD6d8V0LMGjZBPNISMlBEUJ+oPanxyZWOF4ijdMPxjFPTz5iCl1gqnIZcA/jimNbbZNxlBJXc7bc4HtSQ2wfdG+1lUjDE5wD/OmPZR7BZpcsCFLB1PCjuKgm0xCnmW6bR0yrZ5qGC3RJgLxCGBwRkdDyDxT54XlRvtSrkED5HGQKpXEcMsbK5+bZyzcZ/wAahEz7RcGFhlgC+3Iz3/CnG+ETBBI6ZyTGp6n29RTb1roqZgMq+CxDAke49xTluGhBl27ty/M7HBx6+1VjFGHLguQoyw3fMR7VHutmSTejbZNpQwtyo+nakFuY2ZY/MBJ+UPIORnk89T7CkYqG2SMA4yNzLnI7cmo57pkZonkDbE2nYOq9wM9qZbSXm793OMhcjZJgj/69dxczSlssuycfKQ8u5l9ifWq00sqSkRouSwHlEZwemMn86kMjiFUO3cTk/NyvtTkmldyzsoO3C7fSnebbwRiOJQRnu3UeuBUcreaQ8sYG98KSTwPUURzBmePzPLMRwXKcn0p8xgkLTeXn5NuVjz+Pt+FVm2iIx2qAjPExjwc45WmPAbaPDqGBcmMKP0qk8NzIriNTgfdcnoT1z7GqrGJHcROfPKBQW5AHcKfTrTZ7RQwj83CtwRtIBqJtsakMnzBtu1emPSnFBG235vlGGRuGA/z2qNiyEsZXPmjCkL2/z2pLiTYGjFuGbPJPr6496j81WVJISG2jlG+YAdgfao8FldHYYPLYTgfjULSRq+9UBwTyifKR/Ou1Ef2GCO3e5inKKyB4wcfXnmk8twxKSHzBjLDsPUUlziNorRcsu3PPrn1oFxCl0pUthXIkG7hRUrMot2gMynJyhAwOO2aJoJJlIYkbgCDnOcdCaaHupGMMT7UI5LkZbHakiN20ZLssG9gE+akVpY/kIJBzkZxt9x/hUKmEOI7iZyBkyYU5z2PpzTZkQW4EjfKPmVDkfXn+lVZIkKsvlbFP3mbsPT6U2KCNjwpwFO0A9faq8sJVC0UTA7uc9xUc0ZicbSUJOHcnP41H5m64Mkm3hCZCpxvNDiZCHu5kIOMBeWb8ugqrKksq72DpnIzF9f1pfJRYmjeKQZGSZDllpNnlqGIXAUFAWx/+uu08iGK0EdpASI1WIS4/j54556Z55prwpLJmQSxMQfk2feI7AdzUEkDGLbHgZ+8CeTSEeXuEaxEkYCDnn3zUtnLJCjR3GxGTnBX5gD61IzlmDBywbh0TqTUEiLb3DyuAxThV7knsfXFPjZ5IcSojlgFIY/d+gqKTKAJHayO5wWUHJ+ntmo5J8SlJYmDEbmRjgr7/AE9qbAI7edZLm5eRsZ8knKjPp7VHIInjYx3DsBnzWPT8Px/nRG0Zdd6ttIwpTkfXP1qJ2X7QrSosqLnfb+Zt3/j61EkEc6tIrM2OqKOD6flTls4ZPMMcYQrHl2bgfrVNrTZGrRyhSQVDMOq+1QXFusRLmYlW4JA5B7fhUDNCxO2RWPC7iSSfT9P50hYyt50pDdQpY9MdBXdJJDFFBdeeikqxCK3K9qPt0yv5T8i2IMbxJ8yjrkGoglvGxaSXazkMqHv61X2osZJyDnjAzg/WpEhE0klz5pkUxhQccZ9x39aYERYQFmJIP3nXih7eWWRluCQsahwwbIbHPX3p0heFxsYsGwVEnBBxnJNN2SyyGQu0Kty3Gct6fjUcsYRllMryJt3bpDypz+v0qNp08sPudyHPl/Jjk9qiZ5vMkDKIw5BkG3jjt+dMkDwh4ZC21TldnK57fQf40PElsyz7htJ3Mzrgj1Apyu7YjRmKAlgx4z7cUt1MZZXO/ES4wuMk++arLArMqz26qzKSu5u3YgjpTLy3jWLY8T8YEj543e1V7i0D3CRSSbhDIWSWNeXGOD7YqKS0eXLPGHYDDAjByfWuvmMrMXntYYnXj9y+VHrUDiZwLlHU+YP3ikZOB0+lRzLcyyhtx3OPlcnoKWbYsRYzjYh4I4JY1JbKgd237kYZba2CPSnLLLArLy0TdSQCSB29qERXzHHEAjR4Zd2ByfX1p0spdfJjkBCjH385+lROC7mCR1csPly/H1qpc219IHnSMmSMYHP3fcD0p+4uQtt0jOWXphsc9feo7h3kBJ+dgn7zIyT7+9NEsVvktFsYcKwP8/WohCwdpYIVMjtmKSZyQD3Iz3psgDL5EkvlsRueVm4bHYe/oKczbvmtztVVChf7w96c8EuRDEh8wL827GMdgPTFQPCykKsylRxg84H0/rUSsyZljmI3NtZVj556DNEC3jrvggA7KUbk49c1/9k='
data = data.decode()
header = data.split("&")[0]
x_cod = int(header.split("_")[0])
y_cod = int(header.split("_")[1])

x_len = int(header.split("_")[2])
y_len = int(header.split("_")[3])
print((x_cod, y_cod))

img_data = base64.b64decode(data.split("&")[1])
nparr = np.frombuffer(img_data, np.int8)
img_decode = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

baseImg[y_cod:(y_cod + y_len), x_cod:(x_cod + x_len)] = img_decode
cv2.imshow("img", baseImg)
cv2.waitKey()
"""