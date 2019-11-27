import psutil
import time

def cpuStatus ():
     while True:
        print "CPU Usege: %.2f%%" %(psutil.cpu_percent(interval=1))
        print "Memory Usege: %.2f%%" %(psutil.virtual_memory().percent),"(used: %.2f MB / %.2f GB)" %(1.0*psutil.virtual_memory().used/(1024**2), 1.0*psutil.virtual_memory().total/(1024**3))
        print "Disk Usege: %.2f%%" %(psutil.disk_usage('/').percent),"(used: %.2f GB / %.2f TB)" %(1.0*psutil.disk_usage('/').used/(1024**3), 1.0*psutil.disk_usage('/').total/(1024**4))
        time.sleep(5)
     else:
        exit()
cpuStatus()