#                  Step 2: Take photos to add to the dataset
# import the necessary packages
#from firebase import firebase
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import time
import sqlite3
import os
import RPi.GPIO as GPIO
from subprocess import call

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

RED_LED = 21
GREEN_LED = 16

GPIO.setup(RED_LED, GPIO.OUT)
GPIO.setup(GREEN_LED, GPIO.OUT)

conn = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')
c = conn.cursor()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#firebase = firebase.FirebaseApplication('https://smartdoormobileapp.firebaseio.com/')
#name = firebase2.get('/Name', None)
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
camera.vflip = False
rawCapture = PiRGBArray(camera, size=(640, 480))

name = ("Graeme")
#uname = raw_input("Enter your name: ")
c.execute('INSERT INTO users (name) VALUES (?)', (name, ))
uid = c.lastrowid
sampleNum = 0
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
        cv2.imwrite("dataset/User." + str(uid) + "." + str(sampleNum) + ".jpg", gray[y: y + h, x: x + w])
        print("Sample Pic: ", sampleNum)
        sampleNum = sampleNum + 1
        cv2.waitKey(100)
        cv2.imshow('record_faces', image)
        GPIO.output(RED_LED, True)
        cv2.waitKey(3);
        GPIO.output(RED_LED, False)
        time.sleep(0.5)
    if sampleNum > 50:      
        GPIO.output(GREEN_LED, True)
        time.sleep(3)
        GPIO.output(GREEN_LED, False)        
        GPIO.cleanup()
        break

    #cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
 
    # clear the stream in preparation for the next frame
    
    rawCapture.truncate(0)
 
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
            GPIO.cleanup()
	    break

#cap.release()
GPIO.cleanup()
exit_code = call("python trainer.py", shell=True)
conn.commit()
conn.close()
cv2.destroyAllWindows()
