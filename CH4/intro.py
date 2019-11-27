# -*- coding: utf-8 -*-

#BASIC
s = "abcdef"
print s[2:4]
print len(s)
print s[0:6]

#

# startswith
# endswith
# find
# replace
# count

# TEXT AND SENTENCE

# capitalize
# title
# upper
# lower

string = "This is a Python"
# print string.capitalize(string)
# print string.title(string)
# print string.upper(string)
# print string.capitalize(string)

# FORMATTING STRING
# center
# ljust
# rjust

# print string.center(10,"-")

# LIST AND SEQUENCE METHOD
# join
# splitlines
# split

list_data = string.splitlines()
print list_data
print string.split()
print string.split("s")
print string.split("s",1)

#DATETIME

import datetime
now = datetime.datetime.now()
now_utc = datetime.datetime.utcnow()
# print now
print now_utc
# new_date = datetime.datetime(


# DATE TIME FORMAT DIRECTIVE
%a
%A

# %m
# %b

date_str = "10/11/2012 13:14:15"

date = datetime.datetime.strptime(date_str,"%d/%m/%Y")
print date
print type

# strftime แปลงกลับ สตริง
# strptime แปลงไป ไทม์

# COMPARE DATETIME
now = datetime.datetime.now()
print now
print datetime.timedelta(minutes=3)
print now-datetime.timedelta(minutes=5)
print now > datetime.datetime()

# TRY EXCEPT (Error Handling) กลไลในการจัดการความผืดปกติของโปรแกรม

flag = True
while flag:
    try:
        num1 =

# ERROR AND EXCEPTIONS
        
