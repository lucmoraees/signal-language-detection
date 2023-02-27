import tensorflow
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
from cvzone.ClassificationModule import Classifier

cap = cv2.VideoCapture(0)
counter = 0
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")

OFFSET = 20
IMAGE_SIZE = 300  # Tamanha do frame da mão
FOLDER = "Data/C"
LABELS = ["A", "B", "C"]

while True:
    try:
        success, img = cap.read()
        imgOutput = img.copy()
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            imgFrame = np.ones((IMAGE_SIZE, IMAGE_SIZE, 3), np.uint8) * 255

            imgCrop = img[y - OFFSET: y + h +
                          OFFSET, x - OFFSET: x + w + OFFSET]

            imgCropShape = imgCrop.shape

            if h > w:
                k = IMAGE_SIZE / h
                newWidth = math.ceil(w * k)

                imgResize = cv2.resize(imgCrop, (newWidth, IMAGE_SIZE))
                imgResizeShape = imgResize.shape

                widthGap = math.ceil((IMAGE_SIZE - newWidth) / 2)

                imgFrame[:, widthGap: widthGap + newWidth] = imgResize
            else:
                k = IMAGE_SIZE / w
                newHight = math.ceil(h * k)

                imgResize = cv2.resize(imgCrop, (IMAGE_SIZE, newHight))
                imgResizeShape = imgResize.shape

                hightGap = math.ceil((IMAGE_SIZE - newHight) / 2)

                imgFrame[hightGap: hightGap + newHight, :] = imgResize
        

            prediction, index = classifier.getPrediction(imgFrame)
            
            cv2.putText(img, LABELS[index], (x + 100, y - 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)
            # cv2.imshow("ImgFrame", imgOutput)

        cv2.imshow("Image", img)
        cv2.waitKey(1)

    except Exception as e:
        print(e)
