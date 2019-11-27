# -*- coding=utf-8 -*-
import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="203.150.243.40", username="ols-user", password="Natty1990", key_filename="thatsanai.pem")
stdin, stdout, stderr = client.exec_command("df -T /home")
list = stdout.read().split()
print list
print "พื้นที่ที่ถูกใช้งานแล้ว: %2f Gb"%(float(list[11])/(1024**2))
print "พื้นที่ที่ว่างอยู่: %2f Gb"%(float(list[12])/(1024**2))
print "พื้นที่ทั้งหมด: %2f Gb"%(float(list[10])/(1024**2))

client.close()



