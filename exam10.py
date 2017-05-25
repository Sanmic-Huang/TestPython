# ================================================
# Designer: Sanmic Huang
# Goal: Learning
# Date: 2017/04/07
# 
# Run: Fn+F5 Common:CMD+/
# ================================================

# encoding: utf-8

import sys
file_in = file('db.txt','r')
file_out = file('copy.txt','w')
for line in file_in:
    for i in range(0,len(line)):
        if line[i]!="\n":
            sys.stdout.write(line[i]+',')
        else:
            sys.stdout.write(line[i])
        file_out.write(line[i])

sys.stdout.write("\n")
file_in.close()
file_out.close()