import digitalio #pylint: disable-msg=import-error
from digitalio import DigitalInOut, Direction, Pull #pylint: disable-msg=import-error
import time
import board #pylint: disable-msg=import-error
import random #pylint: disable-msg=import-error
print("let's go!")

class FancyLED :
    def __init__(self, p1, p2, p3):
        print("you just made an object!")
        self.L1 = p1
        self.L2 = p2
        self.L3 = p3

        self.L1 = DigitalInOut(p1)
        self.L1.direction = Direction.OUTPUT
        self.L2 = DigitalInOut(p2)
        self.L2.direction = Direction.OUTPUT
        self.L3 = DigitalInOut(p3)
        self.L3.direction = Direction.OUTPUT

    def alternate(self):
        print("alternate now")
        self.L1.value = True 
        self.L2.value = False
        self.L3.value = True
        time.sleep(1)
        self.L1.value = False
        self.L2.value = True
        self.L3.value = False
        time.sleep(0.5)
        self.L2.value = False


    def chase(self):
        self.L1.value = True
        time.sleep(0.1) 
        self.L2.value = True
        time.sleep(0.1) 
        self.L1.value = False
        time.sleep(0.1)
        self.L3.value = True
        time.sleep(0.1)
        self.L2.value = False
        time.sleep(0.1)
        self.L3.value = False
        time.sleep(1)

    def blink(self):
        self.L1.value = True
        self.L2.value = True
        self.L3.value = True
        time.sleep(1)
        self.L1.value = False
        self.L2.value = False
        self.L3.value = False
        time.sleep(1)
    
    def sparkle(self):
        for whatever in range(0,50):
            n= random.randint(0,3) 
            print (n)
            if n==0:
                self.L1.value = True
                self.L2.value = True
                self.L3.value = True
            if n==1:
                self.L1.value = False
                self.L2.value = False
                self.L3.value = True
            if n==2:
                self.L1.value = True
                self.L2.value = False
                self.L3.value = False
            if n==3:
                self.L1.value = False
                self.L2.value = True
                self.L3.value = False
            time.sleep(.05)
            self.L1.value = False
            self.L2.value = False
            self.L3.value = False        