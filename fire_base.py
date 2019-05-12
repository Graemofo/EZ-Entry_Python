# This is a Python 3 Script that will take care of sending images
# to Firebase and opening the smart door via mobile application

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
from subprocess import call

config = {
  "apiKey": "AIzaSyCOAsUtv0LWbKAtB3EiOQuIkWOr-MhPkGE",
  "authDomain": "smartdoormobileapp.firebaseapp.com",
  "databaseURL": "https://smartdoormobileapp.firebaseio.com/",
  "storageBucket": "smartdoormobileapp.appspot.com"
}


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(17, GPIO.OUT) # output GPIO is set to GPIO pin 17

GPIO.output(17, GPIO.HIGH) #Turn relay on as soon as script is run

firebase1 = pyrebase.initialize_app(config) #pyrebase for images
firebase2 = firebase.FirebaseApplication('https://smartdoormobileapp.firebaseio.com/')
storage = firebase1.storage()
# This thread controls the interaction with the unlocking of the door and creating a data set (taking pics)
def door():
    print ('Thread Running: door')
    while True:
        time.sleep(1)
        try:
            create = firebase2.get('/Data', None) # Get value from /data node in Firebasee
            result = firebase2.get('/Door', None) # Get value from /door node in Firebase
            if result == "Open":
                print (result)
                GPIO.output(17, GPIO.LOW)
                time.sleep(30)
                GPIO.output(17, GPIO.HIGH)
            else:
                print (result)
            if create != "null":  # If create is not null, run record_faces script
                exit_code = call("python record_faces.py", shell=True)
                print('Recording Faces')
            else:
                print('Nope')
            
        except KeyboardInterrupt:
            print('Thread Not Running: pull.py')


# Get image from live folder named Visitor and send to the live folder in Firebase
def image():
    print ('Thread Running: image')
    while True:
        print('Image Uploading')
        storage.child("live/Visitor.jpg").put("live/Visitor.jpg")
        time.sleep(1)
    
if __name__ == '__main__':
    Thread(target = door).start()
    Thread(target = image).start()



    
