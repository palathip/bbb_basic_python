# -*- coding: utf-8 -*-
import psutil
import os
# Psutil เป็น Library ที่ใช้เเรียกข้อมูลพื้นฐานของเครื่อง

print psutil.cpu_percent(interval=1)
print psutil.virtual_memory()
print psutil.virtual_memory().used/(1024**3)
print "Used:",psutil.virtual_memory().used/(1024**3),"Gigabyte"
print psutil.disk_usage("/")

#LINE NOTIFY