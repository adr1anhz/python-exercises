import cv2
import time

## Let's say you have a laptop with camera and you want to use that one then use "0" if you want to use the secondary camera example through USB use "1"
video = cv2.VideoCapture(0)
time.sleep(1)
print(help(video.read))   
while True:
    check, frame = video.read()
    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()