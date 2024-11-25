import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

DATA_DIR = './data' #目標資料夾

# 找出每一類的第一張圖片，並且畫出XY軸
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_))[:1]:

        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.figure()
        plt.imshow(img_rgb)
plt.show()