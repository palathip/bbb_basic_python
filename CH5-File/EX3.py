# -*- coding: utf-8 -*-
import threading
import time

def findSquare(wid,long):
    time.sleep(2)
    print "Square:",wid*long

def findcube(wid,long,high):
    time.sleep(3)
    print "Cube:",wid*long*high

w=input("กรุณาใส่ความกว้าง:")
l=input("กรุณาใส่ความยาว:")
h=input("กรุณาใส่ความสูง:")

# Sequence Process
stime = time.time()
findSquare(w,l)
findcube(w,l,h)
print "Sequence process time:",time.time()-stime,"\n"

# Thread Process
stime = time.time()
t1 = threading.Thread(target=findSquare,args=(w,l,))
t2 = threading.Thread(target=findcube,args=(w,l,h,))

t1.start()
t2.start()
t1.join()
t2.join()

print "Thread process time:",time.time()-stime
