from firebase import firebase
import RPi.GPIO as GPIO
import time
import pyrebase
import os
file = open("pull_pid.txt","w") 
file.write(str(os.getpid()))
file.close()

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(17, GPIO.OUT) # output GPIO is set to GPIO pin 17

#GPIO.output(17, GPIO.HIGH)

firebase2 = firebase.FirebaseApplication('https://smartdoormobileapp.firebaseio.com/')

print ('Script Running: pull.py')
while True:
    time.sleep(1)
    try:
        result = firebase2.get('/Door', None)
        if result == "Open":
            #print (result)
            GPIO.output(17, GPIO.LOW)
            time.sleep(30)
        else:
            print (result)
        GPIO.output(17, GPIO.HIGH)
    except KeyboardInterrupt:
        print('Script Not Running: pull.py')




