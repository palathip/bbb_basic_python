import telnetlib

try:
    tn = telnetlib.Telnet("203.150.243.40",80,timeout=2)
    print "telnetsuccess"
    tn.close()
except:
    print "telnet fail"