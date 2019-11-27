

import requests
import threading
import time

def getResponse(url):
    try:
        resp = requests.get(url)
        print url, "Status:",resp.status_code
    except:
        print url, "Fail"

start_time = time.time()

websites = ["http://www.google.com","http://www.facebook.com/admin","http://www.youtube.co.th/","http://www.twitter.com/","http://www.sanook.com/"]
for web in websites:
    getResponse(web)
print "seq process time:", time.time() - start_time,"\n"


start_time = time.time()
threads = []
for website in websites:
    t = threading.Thread(target=getResponse, args=(website,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()
print "thread process time:", time.time() - start_time
