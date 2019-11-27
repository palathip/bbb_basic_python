import os
import telnetlib

host = ["203.161.227.51","google.com","inet.com","203.151.223.57"]
port = ["9999","443"]

for i in range(len(host)):
    print ">>> IP %s <<<" %(host[i])
    ping = os.system("ping "+host[i])
    if ping == 0:
        print "ping: found"
        print "telnet:"
        for j in range(len(port)):
            try:
                telnet = telnetlib.Telnet(host[i],port[j],timeout=2)
                print port[j],"->success"
                telnet.close()
            except:
                print port[j],"->fail"
    else:
        print "ping not found"