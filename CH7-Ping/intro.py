# -*- coding: utf-8 -*-
import os

hostname = "google.com"

import telnetlib #วิธัการติดต่อ รีโมตเครื่องระยะไกล
# tn = telnetlib.Telnet(HOST,PORT)
    try:
        tn = telnetlib.Telnet("8.8.8.8",port=80)
        print "Success"
        tn.close()
    except:
        print "Fail"


