import cv2
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    imlist, box = detector.findPosition(img)
    cv2.imshow("Result", img)
    cv2.waitKey(1)

vid.release()

cv2.destroyAllWindows()