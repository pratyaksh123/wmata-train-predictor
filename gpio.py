import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turn_on_red():
    GPIO.setup(14,GPIO.OUT)
    print("LED on")
    GPIO.output(14,GPIO.HIGH)

def turn_off_red():
    GPIO.setup(14,GPIO.OUT)
    GPIO.output(14,GPIO.LOW)
    
def turn_off_green():
    GPIO.setup(15,GPIO.OUT)
    GPIO.output(15,GPIO.LOW)

def turn_on_green():
    GPIO.setup(15,GPIO.OUT)
    print("LED on")
    GPIO.output(15,GPIO.HIGH)    


# turn_off_red()