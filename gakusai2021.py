# @Date:   2021-09-12T18:09:19+09:00
# @Last modified time: 2021-09-14T19:59:44+09:00



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

except KeyboardInterrupt:
    GPIO.cleanup()
    exit()

def　right_rotation(): #砲塔の右旋回
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
    rightMotorPwm.ChangeDutyCycle(0)
    leftMotorPwm.ChangeDutyCycle(0)
    time.sleep(0.1)
    return

def straight():
    rightMotorPwm.ChangeDutyCycle(100)
    leftMotorPwm.ChangeDutyCycle(100)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.1)
    return

def right():
    rightMotorPwm.ChangeDutyCycle(50)
    leftMotorPwm.ChangeDutyCycle(100)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.1)
    return

def left():
    rightMotorPwm.ChangeDutyCycle(100)
    leftMotorPwm.ChangeDutyCycle(50)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.1)
    return

def back():
    rightMotorPwm.ChangeDutyCycle(100)
    leftMotorPwm.ChangeDutyCycle(100)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    time.sleep(0.1)
    return

def back_right():
    rightMotorPwm.ChangeDutyCycle(50)
    leftMotorPwm.ChangeDutyCycle(100)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    time.sleep(0.1)
    return

def back_left():
    rightMotorPwm.ChangeDutyCycle(100)
    leftMotorPwm.ChangeDutyCycle(50)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(5,GPIO.LOW)
    time.sleep(0.1)
    return

def right_turn(): #右旋回
    rightMotorPwm.ChangeDutyCycle(100)
    leftMotorPwm.ChangeDutyCycle(100)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(5,GPIO.HIGH)
    time.sleep(0.1)
    return

def left_turn(): #左旋回
    rightMotorPwm.ChangeDutyCycle(100)
    leftMotorPwm.ChangeDutyCycle(100)
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(25,GPIO.HIGH)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(5,GPIO.LOW)
    time.sleep(0.1)
    return
