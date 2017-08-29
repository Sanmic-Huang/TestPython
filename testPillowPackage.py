# ===========================================
# Designer: Sanmic Huang
# Date: 2017/08/29
# SOP: shift+CMD+D, fn+F5, cmd+W
# GIT: shift+Ctl+G, Keyin submit, cmd+enter
# Goal: Test pillow package
# ===========================================
from PIL import Image

path='/Volumes/SanmicSD/0-Backup/Code/1-DB/Lena/BW/'
filename='Lena512BW.png'
img = Image.open(path+filename)
img.show()
