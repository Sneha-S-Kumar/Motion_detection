import cv2
import cv2 
import time
import datetime
import datetime 
import smtplib, ssl

s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security   
s.starttls()

# Authentication  
s.login("smartsurvelliancemini@gmail.com", "dprczumxpgyqgijj")


# message to be sent   
SUBJECT = "ALERT!!"   
TEXT = "MOTION DETECTED"

message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

cap = cv2.VideoCapture(0) #to set the camera
#cap = cv2.VideoCapture('http://192.168.167.87:8080/video')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml") 
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_fullbody_default.xml") 
@@ -13,6 +30,10 @@
SECONDS_TO_RECORD_AFTER_DETECTION = 5






frame_size = (int(cap.get(3)),int(cap.get(4))) #to record the video we need frame size
fourcc = cv2.VideoWriter_fourcc(*"mp4v") #to save the video in mp4

@@ -30,6 +51,11 @@
             current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S") #to get the date and time for the recorded video
             out = cv2.VideoWriter(f"{current_time}.mp4", fourcc, 20, frame_size)
             print("START RECORDING")
             # sending the mail    
             s.sendmail("smartsurvelliancemini@gmail.com", "a.sankar2310@gmail.com", message)

             # terminating the session    
             s.quit()

    elif detection :
        if timer_started:
@@ -61,3 +87,5 @@
cap.release()
cv2.destroyAllWindows()
