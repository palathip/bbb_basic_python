# -*- coding: utf-8 -*- # Encoding ภาษาไทย

#การใส่ input str
print "Welcome to day 1\n INET PYTHON TRAINING"
z = "Hello World"
x = raw_input("Input 1:") #raw_input รับ str ได้
y = raw_input("Input 2:") #กรอกข้อมูลชุดที่ 2
print z,x,y

#str(var) #เป็นการ convert ตัวแปร
# การ *1.0 คือการแปลงเป็น float

print "\nBasic Plus Calculator"
a = input("First Number:")
b = input("Second Number")

# str(c) #เป็นการ convert ตัวแปร
print "\nYour Result:%.5d" %(a+b)
print "\nYour Result:%.5f" %(a+b)
print "\nYour Result:%s" %(a+b)

# type(var) ตรวจสอบตัวแปร

# Operand
# // หารปัดเศษ
# % Mod หารเอาเศษ
# ** Power