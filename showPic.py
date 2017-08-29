# ===========================================
# Designer: Sanmic Huang
# Date: 2017/08/29
# shift+CMD+D, fn+F5, cmd+W
# ===========================================
import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('Lena512BW.png', 0)
img = cv2.imread('/Volumes/SanmicSD/0-Backup/Code/1-DB/Lena/BW/Lena512BW.png', 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
