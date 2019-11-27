# -*- coding=utf-8 -*-
import paramiko
import time
import requests

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname="203.150.243.40", username="ols-user", password="Natty1990", key_filename="thatsanai.pem")
stdin, stdout, stderr = client.exec_command("df -T /home")
list = stdout.read().split()
print list
print "พื้นที่ที่ถูกใช้งานแล้ว: %2f Gb"%(float(list[11])/(1024**2))
print "พื้นที่ที่ว่างอยู่: %2f Gb"%(float(list[12])/(1024**2))
print "พื้นที่ทั้งหมด: %2f Gb"%(float(list[10])/(1024**2))
disk_percent = ((float(list[11])/(1024**2))/(float(list[10])/(1024**2)))*100
print disk_percent

client.close()

def lineNotify(show):
    url = "https://notify-api.line.me/api/notify"

    payload = "message= %s" %show
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Bearer DozJII5KtXLyajw2iGz3ebKYC0LXY8fVek709idDnTx",
        'cache-control': "no-cache",
        'Postman-Token': "b4c6e079-3401-4919-9a8b-6205e7e524ad"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

def overUsed():
    sw1 = True
    while sw1:
         time.sleep(30)
         if disk_percent > 50:
             message = "DETECT"
             lineNotify(message)
             print "Active loop 1 if"
             sw2 = True
             while sw2: #เงื่อนไขนี้อาจจะ ใช้ Check  Back to normal ใน EX2 บท Line Notify ได้ดีกว่าเดิม ไว้ค่อยลอง
                    if disk_percent > 50:
                        time.sleep(5)
                        print "Active loop 2 if"
                        message = "DETECT"
                        lineNotify(message)
                    else:
                        message = "Back to normal"
                        lineNotify(message)
                        print "Active loop 2 else"
                        sw2 = False

overUsed()
