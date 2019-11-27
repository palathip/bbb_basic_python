import datetime

now = datetime.datetime.now()
for i in range(1,8):
    day_format = datetime.datetime.strftime(now-datetime.timedelta(days=i), "%A, %d-%m-%Y %H:%M:%S %p")
    print day_format
