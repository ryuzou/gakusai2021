# @Date:   2021-11-03T16:06:31+09:00
# @Last modified time: 2021-11-04T22:59:23+09:00


import pigpio
import time
import posix_ipc
import json

A_PWM = 12
B_PWM = 18

A_IN_1 = 23
A_IN_2 = 24
B_IN_1 = 25
B_IN_2 = 16

STBY = 17

LASER_GUN = 21

pi = pigpio.pi()

# Setup

OUTPUT_PINS = [A_PWM, B_PWM, A_IN_1, A_IN_2, B_IN_2, B_IN_1, STBY]
for PINS in OUTPUT_PINS:
    pi.set_mode(PINS, pigpio.OUTPUT)
pi.write(STBY, 1)

mq = posix_ipc.MessageQueue("/gakusai2021.1")

# End Setup

def stop():
    pi.write(STBY, 0)
    return
def move_A(dir, radius):
    if dir == "foward":
        pi.write(A_IN_1, 0)
        pi.write(A_IN_2, 1)
    elif dir == "back":
        pi.write(A_IN_1, 1)
        pi.write(A_IN_2, 0)
    else:
        print("dir err (motor A)")
    pi.set_PWM_dutycycle(A_PWM, radius)
def move_B(dir, radius):
    if dir == "foward":
        pi.write(B_IN_1, 0)
        pi.write(B_IN_2, 1)
    elif dir == "back":
        pi.write(B_IN_1, 1)
        pi.write(B_IN_2, 0)
    else:
        print("dir err (motor B)")
    pi.set_PWM_dutycycle(B_PWM, radius)


def move(radius, stick_degree):
    if 0 <= stick_degree < 3:  # 直進
        rightPwm = 100
        leftPwm = 100
    elif 3 <= stick_degree < 87:  # 右前方
        rightPwm = 100 - (stick_degree - 3)
        leftPwm = 100
    elif 87 <= stick_degree < 93:  # 右旋回
        rightPwm = 50
        leftPwm = 50
    elif 93 <= stick_degree < 177:  # 右後方
        rightPwm = 100 - (177 - stick_degree)
        leftPwm = 100
    elif 177 <= stick_degree < 183:  # 後退
        rightPwm = 100
        leftPwm = 100
    elif 183 <= stick_degree < 267:  # 左後方
        rightPwm = 100
        leftPwm = 100 - (stick_degree - 183)
    elif 267 <= stick_degree < 273:  # 左旋回
        rightPwm = 50
        leftPwm = 50
    elif 273 <= stick_degree < 357:  # 左前方
        rightPwm = 100
        leftPwm = 100 - (357 - stick_degree)
    elif 357 <= stick_degree <= 360:  # 直進
        rightPwm = 100
        leftPwm = 100
    if radius <= 70:  # 低速
        rightPwm *= 0.5
        leftPwm *= 0.5
    if 0 <= stick_degree < 87 or 273 <= stick_degree <= 360:  # 前方
        move_A("foward", radius = rightPwm)
        move_B("foward", radius = leftPwm)
    elif 93 <= stick_degree < 267:  # 後方
        move_A("back", radius = rightPwm)
        move_B("back", radius = leftPwm)
    elif 87 <= stick_degree < 93:  # 右旋回
        move_A("foward", radius = rightPwm)
        move_B("back", radius = leftPwm)
    elif 267 <= stick_degree < 273:  # 左旋回
        move_A("back", radius = rightPwm)
        move_B("foward", radius = leftPwm)
    time.sleep(0.1)
    stop()

while True:
    mqs = mq.receive()
    movementJsonCode = json.loads(mqs[0].decode())
    radius = movementJsonCode["joystick"]["radius"]
    stick_degree = movementJsonCode["joystick"]["stick_degree"]
    shot_button = movementJsonCode["shot_button"]
    reload_button = movementJsonCode["reload_button"]
    left = movementJsonCode["left"]
    right = movementJsonCode["right"]
    move(radius, stick_degree)

