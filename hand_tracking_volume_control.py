"""
(PROJECT)
Hand tracking: Gesture volume control for MacOS

This project implements cvzone.HandTraclingModule
for MacOS volume control you can run this code
and use your index fingers and your Tumb
for controlling the volume.
"""

import cv2
import subprocess
from cvzone.HandTrackingModule import HandDetector

TEXT_COLOR = (255, 188, 91)
TEXT_SIZE = 3
TEXT_THICK = 5

webcam = cv2.VideoCapture(0)
detector = HandDetector(detectionCon = 0.8, maxHands = 2)

while True:
    _, frame = webcam.read()

    # Hands Detection
    hands, img = detector.findHands(frame)
    if hands:
        hand_1 = hands[0]
        hand_1_type = hand_1["type"]
        hand_1_bbox = hand_1["bbox"]
        hand_1_center = hand_1["center"]
        hand_1_lmList = hand_1["lmList"]

        hand_1_fingers = detector.fingersUp(hand_1)

        if len(hands) == 2:
            hand_2 = hands[1]
            hand_2_type = hand_2["type"]
            hand_2_bbox = hand_2["bbox"]
            hand_2_center = hand_2["center"]
            hand_2_lmList = hand_2["lmList"]

            hand_2_fingers = detector.fingersUp(hand_2)

            """
            OUTPUT FOR 2 HANDS
            ------------------
            PUT SOME CODE HERE
            IF YOU WANT...
            """
        elif len(hands) == 1:
            """
            OUTPUT FOR 1 HAND
            ------------------
            PUT SOME CODE HERE
            IF YOU WANT...
            """
            length, info, frame = detector.findDistance(hand_1_lmList[4][0:2], hand_1_lmList[8][0:2], frame, scale = 7)
            if 150 <= length <= 550:
                volume = (length-200)/300   # Length scale 200 - 500 -> Volume scale 0 - 100
                if volume >= 1: volume = 1
                if volume <= 0: volume = 0
                subprocess.run([f"osascript -e \"set volume output volume {(volume * 100):.2f}\""], shell = True)

    # If you don't need to show your webcam video you just comment line 64 away.
    cv2.imshow("WebcamVideo", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

webcam.release()
cv2.destroyAllWindows()
cv2.waitKey(-1)
