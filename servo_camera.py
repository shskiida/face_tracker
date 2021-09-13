#!/usr/bin/env python

import cv2
import sys
import time
import Adafruit_PCA9685


width = 320
height = 240

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

caspath = 'haarcascade_frontalface_default.xml'
Cascade = cv2.CascadeClassifier(caspath)

vs =cv2.VideoCapture(0)
vs.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def move_x(x):
    pwm.set_pwm(0, 0, x)
    
def move_y(y):
    pwm.set_pwm(1, 0, y)
    
    
    

move_x(350)
move_y(350)

now_x = 350
now_y = 350

while True:
    ret,frame = vs.read()

    if ret == False:
        print('error has occurred')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #顔を検出
    faces = Cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(10,10))

    for (x,y,w,h) in faces:
        #検出した顔に四角形を描く
        cv2.rectangle(frame, (x,y),(x+w, y+h),(255, 0, 0),2)

        #四角形の中心地を計算
        center_x = x + (w/2)
        center_y = y + (h/2)

        go_x = now_x - (center_x - (width/2))*0.12
        go_y = now_y + (center_y - (height/2))*0.12

        print(now_x-go_x,now_y-go_y)
        if not 1 > now_x-go_x > -1:
            move_x(int(go_x))
            now_x = go_x
        
        if not 1 > now_y-go_y > -1:
            move_y(int(go_y))
            now_y = go_y

    cv2.imshow("video", frame)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

        


        
        
        

    
