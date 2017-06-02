# ============================================================================
# Designer: Sanmic Huang
# Site: httt://sanmic.lit.edu.tw
# Date: 2017/05/25
# Goal: Serial Communication
# Docs: http://pythonhosted.org/pyserial/  http://pythonhosted.org/pyserial/
# Version: 1.0.0
# Description:
# Note: ls /dev/tty.*
# Run: Fn+F5 Comment:CMD+/ Terminal:^`
# ============================================================================
# encoding: utf-8

import serial
s=serial.Serial('/dev/tty.usbmodem1421',9600)
while True: print s.readline()