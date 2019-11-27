import time
import threading

def findMax(number,delay):
    print "finding max ..."
    time.sleep(delay)
    print "MAX:",max(number)

def findMin(number,delay):
    print "finding min ..."
    time.sleep(delay)
    print "MIN:",min(number)

s_time = time.time()
arr = [10,7,29,62,19]
print arr
delay1 = 3
delay2 = 5

findMax(arr,delay1)
findMin(arr,delay2)
print "Seq Process Time :",time.time()-s_time

t_time = time.time()
t1 = threading.Thread(target=findMax,args=(arr,delay1,))
t2 = threading.Thread(target=findMin,args=(arr,delay2,))

t1.start()
t2.start()

t1.join()
t2.join()

print "Thread Process Time :", time.time()-t_time