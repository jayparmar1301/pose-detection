################################################
# Developer Jay Parmar 
# https://github.com/jayparmar1301
################################################

#required libraries
import cv2
import time
import mediapipe as mp

# initializing mediapip library
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


# if you wish to detect post from any video
# cap = cv2.VideoCapture('videoplayback.mp4')

# it will detect post from webcab of your laptop/pc
cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success, frame = cap.read()
    imgRBG = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = pose.process(imgRBG)
    print(result.pose_landmarks)
    if result.pose_landmarks:
        mpDraw.draw_landmarks(imgRBG, result.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(result.pose_landmarks.landmark):
            h, w, c = imgRBG.shape
            cX, cY = int(lm.x * int(w)), int(lm.y * int(h))
            cv2.circle(imgRBG, (cX, cY), 5, (255, 0, 0), cv2.FILLED)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)),(70,50),cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    cv2.imshow("Video",imgRBG)
    cv2.waitKey(1)