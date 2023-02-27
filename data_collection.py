import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
counter = 0

OFFSET = 20
IMAGE_SIZE = 300  # Tamanha do frame da mão
FOLDER = "Data/C"

while True:
    try:
        success, img = cap.read()
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']

            # Matriz nxn com valores de 0 a 255
            imgFrame = np.ones((IMAGE_SIZE, IMAGE_SIZE, 3), np.uint8) * 255

            # Frame enquadrando apenas a mão
            imgCrop = img[y - OFFSET: y + h +
                          OFFSET, x - OFFSET: x + w + OFFSET]

            imgCropShape = imgCrop.shape

            if h > w:
                # Calculando a proporção entre o IMAGE_SIZE e a altura
                k = IMAGE_SIZE / h

                # Calculando a nova largura de acordo com a proporção
                newWidth = math.ceil(w * k)

                # Redimencionando a imagem de acordo com a nova largura e o IMAGE_SIZE (Altura fixa)
                imgResize = cv2.resize(imgCrop, (newWidth, IMAGE_SIZE))

                imgResizeShape = imgResize.shape

                # Calculando quando de sobra possui entre o IMAGE_SIZE e a nova largura
                widthGap = math.ceil((IMAGE_SIZE - newWidth) / 2)

                # Preencher o frame com os valores da imagem após o redimencionamento + centralização a partir do gap
                imgFrame[:, widthGap: widthGap + newWidth] = imgResize
            else:
                # Calculando a proporção entre o IMAGE_SIZE e a largura
                k = IMAGE_SIZE / w

                # Calculando a nova largura de acordo com a proporção
                newHight = math.ceil(h * k)

                # Redimencionando a imagem de acordo com a nova altura e o IMAGE_SIZE (Altura fixa)
                imgResize = cv2.resize(imgCrop, (IMAGE_SIZE, newHight))

                imgResizeShape = imgResize.shape

                # Calculando quando de sobra possui entre o IMAGE_SIZE e a nova altura
                hightGap = math.ceil((IMAGE_SIZE - newHight) / 2)

                # Preencher o frame com os valores da imagem após o redimencionamento + centralização a partir do gap
                imgFrame[hightGap: hightGap + newHight, :] = imgResize

            cv2.imshow("ImgFrame", imgFrame)

        cv2.imshow("Image", img)

        key = cv2.waitKey(1)

        if key == ord("s"):
            counter += 1
            cv2.imwrite(f'{FOLDER}/Image_{time.time()}.jpg', imgFrame)
            print(counter)

    except Exception as e:
        print(e)
