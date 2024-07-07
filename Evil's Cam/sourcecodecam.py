import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    div = cv2.absdiff(frame1,frame2)
    clr= cv2.cvtColor(div,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(clr,(5,5),0)
    _,thresh= cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dia= cv2.dilate(thresh,None,iterations=5)
    contours,_=cv2.findContours(dia,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    for i in contours:
        if cv2.contourArea(i)<3000:
            continue
        x,y,w,h= cv2.boundingRect(i)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        winsound.Beep(1000,200)
    if cv2.waitKey(10)==ord('a'):
        break
    cv2.imshow("Evil's Cam",frame1)
