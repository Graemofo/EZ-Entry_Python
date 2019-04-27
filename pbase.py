
import pyrebase
import time
import os
file = open("pbase_pid.txt","w") 
file.write(str(os.getpid()))
file.close()

config = {
  "apiKey": "AIzaSyCOAsUtv0LWbKAtB3EiOQuIkWOr-MhPkGE",
  "authDomain": "smartdoormobileapp.firebaseapp.com",
  "databaseURL": "https://smartdoormobileapp.firebaseio.com/",
  "storageBucket": "smartdoormobileapp.appspot.com"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

print ('Script Running: pbase.py')
while True:
    storage.child("live/Visitor.jpg").put("live/Visitor.jpg")
    time.sleep(1)
    #print ("Working")
#storage.child("face.png").put("face.png")
#storage.child("images/Graeme.jpeg").download("images/Graeme.jpeg")

print ("Pyrebase Works")
