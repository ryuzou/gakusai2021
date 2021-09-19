# @Date:   2021-09-12T18:09:19+09:00
# @Last modified time: 2021-09-19T19:35:54+09:00



import RPi.GPIO as GPIO
import pigpio
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)

rightMotorPwm = GPIO.PWM(22,50)
leftMotorPwm = GPIO.PWM(25,50)

rightMotorPwm.start(0)
leftMotorPwm.start(0)

pi = pigpio.pi()
pi.setmode(19,pigpio.OUTPUT)
pi.set_PWM_frequency(19,50)
pi.set_PWM_range(19,2000) #-90°:50 0°:145 90°:240 5°刻み(19刻み)で動く

pulse =145 #初期設定（砲塔0°、モーター停止）
pi.set_PWM_dutycycle(19,145)
stop()

try:
    while 1:
        #以下、入力に対して機体を動かすプログラム
        #left,right,shot,radius,angle
        if shot == 1:
            shot()

        if right + left == 1:
            if right == 1:
                right_rotation()
            if left == 1:
                left_rotation()


        if radius < ○○○ : #停止
            stop()
        else:
            move() < ○○○ : #動く


except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

def shot(): #レーザーガン班
    return

def right_rotation(): #砲塔の右旋回
    if pulse < 240:
        pulse += 19
        pi.set_PWM_dutycycle(19,pulse)
        time.sleep(10**(-6))
        return

def left_rotation(): #砲塔の左旋回
    if pulse > 50:
        pulse -= 19
        pi.set_PWM_dutycycle(19,pulse)
        time.sleep(10**(-6))
        return

#dcモーター１が右前輪、dcモーター２が左前輪
def stop():
        GPIO.output(22,GPIO.LOW)
        GPIO.output(25,GPIO.LOW)
    return

def move(radius, angle):
    if angle < 15: #直進
        rightPwm = 100
        leftPwm = 100
    elif angle < 75: #右前方
        rghtPwm = 100 - (angle - 15)
        leftPwm = 100
    elif angle < 105: #右旋回
        rightPwm = 50
        leftPwm = 50
    elif angle < 165: #右後方
        rightPwm = 100 - (165 - angle)
        leftPwm = 100
    elif angle < 195: #後退
        rightPwm = 100
        leftPwm = 100
    elif angle < 255: #左後方
        rightPwm = 100
        leftPwm = 100 - (angle - 195)
    elif angle < 285: #左旋回
        rightPwm = 50
        leftPwm = 50
    elif angle < 345: #左前方
        rightPwm = 100
        leftPwm = 100 - (345 - angle)
    elif angle < 360: #直進
       rightPwm = 100
        leftPwm = 100

    if radius < ○○○ : #低速
        rightPwm *= 0.5
        leftPwm *= 0.5

    rightMotorPwm.ChangeDutyCycle(rightPwm)
    leftMotorPwm.ChangeDutyCycle(leftPwm)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)

    if 0 <= angle < 75 or 285 <= angle < 360: #前方
        GPIO.output(27,GPIO.LOW)
        GPIO.output(5,GPIO.HIGH)
    elif 105 <= angle < 255: #後方
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(5,GPIO.LOW)
    elif 75 <= angle < 105: #右旋回
        GPIO.output(27,GPIO.HIGH)
        GPIO.output(5,GPIO.HIGH)
    elif 255 <= angle < 285: #左旋回
        GPIO.output(27,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
    time.sleep(0.1)

    return
