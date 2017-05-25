# ================================================
# Designer: Sanmic Huang
# Goal: Learning
# Date: 2017/04/07
# Class的初始化函式是由兩條底線包含著init做宣告。
# Run: Fn+F5 Comment:CMD+/
# ================================================

# encoding: utf-8

class Student:  
    def __init__(self, name, grade, age):  #Class的初始化函式是由兩條底線包含著init做宣告。
        self.name = name  
        self.grade = grade  
        self.age = age  
    def set_name(self, name):  
        self.name = name  

student_objects=[]
student_objects.append( Student('john', 'B', 15) )
student_objects.append( Student('dave', 'A', 12) )
student_objects.append( Student('jane', 'A', 10) )
student_objects[0].set_name('John')

for i in student_objects:
    print i.name,i.grade,i.age 