# -*- coding: utf-8 -*-
#OPEN

f = open(fliename,mode)
with open(fliename,mode) as f:

# MODE
# r
# w
# a
# r+
# w+
# a+


#OPEN
f = open("testfile.txt",mode)
f.write("Hello World\n")
f.write("How are you\n")
f.close()

#WITH OPEN
with open("testfile.txt",mode) as f:
    f.write("Hello World\n")
    f.write("How are you\n")
# End Text Indance and close file

#READ
f = open("testfile.txt",r)
print f.read() #READ ALL
print f.readline() #LINE READ
print f.readlines() #LINE LIST OF STRING
f.close()

#READ LOOP
with open("text.txt",mode) as f
    for i in range(5)

# Loader = yaml.FullLoader


# THREAD
#
# (26-28 เขียน code thread ดู)
# (28-30 เขียน code ดู)
import threading

     t = threading.Thread(target=function,args=(value,)) # รูปแบบ
     t.start()
     t.join() # ประมวลผลเสร็จแล้วรอแสดงผลพร้อมกัน หากไม่ใส่ function ไหนเสร็จก่อนแสดงผลเลย

# import request # ใช้ในการติดต่อ API ในเรียกหรือจัดการหน้า HTTP (บทต่อไป)


