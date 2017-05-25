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
ser = serial.Serial('/dev/tty.usbserial-ftDH24JC')  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
s = ser.read(10)        # read up to ten bytes (timeout)
ser.write(b'hello')      # write a string
line = ser.readlines()   # read a '\n' terminated line
print(s)
print(line)
ser.close()             # close port