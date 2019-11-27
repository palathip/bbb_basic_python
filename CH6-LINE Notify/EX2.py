import psutil
import time
import requests

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


def cpuStatus ():
    prev_cpu_used = 100
    prev_ram_used = 100
    prev_disk_used = 100
    while True:
        cpu_used = psutil.cpu_percent(interval=1)
        ram_used = psutil.virtual_memory().percent
        disk_used = psutil.disk_usage('/').percent

        # print "CPU Usege: %.2f%%" %(cpu_used)
        # print "Memory Usege: %.2f%%" %(ram_used)
        # print "Disk Usege: %.2f%%" %(disk_used)
        print cpu_used
        print ram_used
        print disk_used

        if cpu_used >= 50:
            massege = "CPU Warning : CPU Usege :%.2f percent" %(cpu_used)
            prev_cpu_used = cpu_used
            print massege
            lineNotify(massege)
        elif cpu_used >= 70:
            massege = "CPU Critical : CPU Usege :%.2f percent" %(cpu_used)
            prev_cpu_used = cpu_used
            lineNotify(massege)
        elif prev_cpu_used < 50 and cpu_used < 50:
            massege = "CPU back to normal"
            prev_cpu_used = cpu_used
            lineNotify(massege)

        elif ram_used >= 50:
            massege = "RAM Warning : RAM Usege :%.2f percent" %(ram_used)
            prev_ram_used = ram_used
            lineNotify(massege)
        elif ram_used >= 70:
            massege = "RAM Critical : RAM Usege :%.2f percent" %(ram_used)
            prev_ram_used = ram_used
            lineNotify(massege)
        elif prev_ram_used < 50 and ram_used :
            massege = "RAM back to normal"
            prev_ram_used = ram_used
            lineNotify(massege)

        elif disk_used >= 50:
            massege = "DISK Warning : DISK Usege :%.2f percent" %(disk_used)
            prev_disk_used = disk_used
            lineNotify(massege)
        elif disk_used >= 70:
            massege = "DISK Critical : DISK Usege :%.2f percent" %(disk_used)
            prev_disk_used = disk_used
            lineNotify(massege)
        elif prev_disk_used < 50 and disk_used < 50:
            massege = "DISK back to normal"
            prev_disk_used = disk_used
            lineNotify(massege)
        time.sleep(10)

cpuStatus()



