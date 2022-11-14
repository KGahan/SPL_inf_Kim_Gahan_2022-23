import RPi.GPIO as GPIO
import time

gOr = False

def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.OUT)
        GPIO.output(4,False)
        GPIO.setup(3,GPIO.OUT)
        GPIO.setup(2,GPIO.OUT)
        print("Type Enter to change the traffic light")
        GPIO.output(4,True)
        GPIO.output(3,False)
        GPIO.output(2,False)
        
def changeState():
    global gOr
    if gOr == False:
        gOr = True
        GPIO.output(3,True)       
        time.sleep(1)
        GPIO.output(4,False)
        GPIO.output(3,False)
        GPIO.output(2,True)
    else:
        gOr = False
        GPIO.output(2,True)
        time.sleep(0.5)
        GPIO.output(2,False)
        time.sleep(0.5)
        GPIO.output(2,True)
        time.sleep(0.5)
        GPIO.output(2,False)
        time.sleep(0.5)
        GPIO.output(2,True)
        time.sleep(0.5)
        GPIO.output(2,False)
        time.sleep(0.5)
        GPIO.output(2,True)
        time.sleep(0.5)
        GPIO.output(2,False)
        time.sleep(0.5)
        GPIO.output(2,False)
        GPIO.output(3,True)
        time.sleep(1)
        GPIO.output(3,False)
        GPIO.output(4,True)
    
setup()
while True:
    _input = str(input())
    if _input == "":
        changeState()
    else:
        print("Wrong input!")