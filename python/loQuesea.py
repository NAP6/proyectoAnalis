import numpy as np
import cv2
import imutils
import socketio
import base64
import time

sio = socketio.Client()

sio.connect('http://localhost:80')
sio.emit("authentication", {"username": "nicolas", "password": "1234"})


@sio.event
def connect():
    print("I'm connected!")


@sio.event
def connect_error():
    print("The connection failed!")
    sio.emit("authentication", {"username": "nicolas", "password": "1234"})


@sio.event
def disconnect():
    print("I'm disconnected!")
    sio.emit("authentication", {"username": "nicolas", "password": "1234"})


vs = cv2.VideoCapture(0)

while True:
    # read the next frame from the file
    (grabbed, frame) = vs.read()

    # if the frame was not grabbed, then we have reached the end
    # of the stream
    if not grabbed:
    	break

    

    _, im_arr = cv2.imencode('.jpg', frame)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)
    data = {}
    data['img'] = im_b64
    data['username'] = 'nicolas'
    print('envia')
    sio.emit('pythonServer', data)
    time.sleep(2)
