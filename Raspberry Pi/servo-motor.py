import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
pwm=GPIO.PWM(7, 50)
pwm.start(0)
def setAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(7, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(7, False)
    pwm.ChangeDutyCycle(0)
setAngle(90)
sleep(1)
setAngle(45)
sleep(0)
setAngle(0)
pwm.stop()
GPIO.cleanup()
