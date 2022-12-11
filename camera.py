import cv2
import cvzone
from cvzone.SerialModule import SerialObject
image_counter = 0
video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
while True:
    check, frame = video.read()
    gray_f = cv2.flip(frame, 2)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray_flip = cv2.flip(frame, 1)
    cv2.imshow("kara", gray_flip)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()