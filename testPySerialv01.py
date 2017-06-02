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

import pyfirmata
pin=13
port='/dev/tty.usbmodem1421'
board=pyfirmata.Arduino(port)
board.digital[pin].write(0)
time.sleep(1000)
board.digital[pin].write(1)
time.sleep(1000)
board.digital[pin].write(0)
time.sleep(2)
board.digital[pin].write(1)
time.sleep(2)