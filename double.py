
from firebase import firebase
from time import sleep
import time, math
import RPi.GPIO as GPIO
from threading import Thread
from firebase import firebase
import RPi.GPIO as GPIO
import time
import pyrebase
import os
from firebase import firebase

config = {
  "apiKey": "AIzaSyCOAsUtv0LWbKAtB3EiOQuIkWOr-MhPkGE",
  "authDomain": "smartdoormobileapp.firebaseapp.com",
  "databaseURL": "https://smartdoormobileapp.firebaseio.com/",
  "storageBucket": "smartdoormobileapp.appspot.com"
}


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(17, GPIO.OUT) # output GPIO is set to GPIO pin 17


firebase1 = pyrebase.initialize_app(config) #pyrebase for images
firebase2 = firebase.FirebaseApplication('https://smartdoormobileapp.firebaseio.com/')
storage = firebase1.storage()
def door():
    print ('Thread Running: pull.py')
    while True:
        time.sleep(1)
        try:
            result = firebase2.get('/Door', None)
            if result == "Open":
                print (result)
                GPIO.output(17, GPIO.LOW)
                time.sleep(30)
            else:
                print (result)
            GPIO.output(17, GPIO.HIGH)
        except KeyboardInterrupt:
            print('Thread Not Running: pull.py')


def image():
    print ('Thread Running: pbase.py')
    while True:
        print('Image Uploading')
        storage.child("live/Visitor.jpg").put("live/Visitor.jpg")
        time.sleep(1)
    
if __name__ == '__main__':
    Thread(target = door).start()
    Thread(target = image).start()



    
