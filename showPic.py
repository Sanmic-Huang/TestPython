# ===========================================
# Designer: Sanmic Huang
# Date: 2017/08/29
# SOP: shift+CMD+D, fn+F5, cmd+W
# GIT: shift+Ctl+G, Keyin submit, cmd+enter
# ===========================================
import cv2
import numpy as np
from matplotlib import pyplot as plt

# img = cv2.imread('Lena512BW.png', 0)
# img = cv2.imread('/Volumes/SanmicSD/0-Backup/Code/1-DB/Lena/BW/Lena512BW.png', 0)
path='/Volumes/SanmicSD/0-Backup/Code/1-DB/Lena/BW/'
filename='Lena512BW.png'
img = cv2.imread(path+filename, 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
