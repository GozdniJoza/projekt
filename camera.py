from tkinter import Frame, font
import cv2
from matplotlib import pyplot as plt


vid = cv2.VideoCapture(0)

vid.set(3, 640) # set width as 640
vid.set(4, 480) # set height as 480

# importing cascade
#faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "frontface.xml")
faceCascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
bodyCascade = cv2.CascadeClassifier('cascades/haarcascade_fullbody.xml')


#type of font
font = cv2.FONT_HERSHEY_DUPLEX

while(True):
    #capture frame from videos
    ret, frame = vid.read()
    
    
    #convert to gray img
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #corners around face
    faces = faceCascade.detectMultiScale(frame, 1.3, 4)
    body = bodyCascade.detectMultiScale(frame, 4.5, 10)  
    
    #draw bounding box
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv2.putText(frame, 'Face', (x, y - 5), font, 1, (0, 255, 0), 1, cv2.LINE_4)
    
    #draw bounding box
    for (x, y, w, h) in body:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
        cv2.putText(frame, 'Face', (x, y - 5), font, 1, (0, 255, 0), 1, cv2.LINE_4)
    
    
    cv2.imshow('Face detection', frame)

    #bind to close cam window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()