import datetime

def birthDate():
    print ("Please Enter Your Infomation.")
    b_date = raw_input("Date:")
    b_month = raw_input("Month:")
    b_year = raw_input("Year:")

    birth = datetime.datetime.strptime(b_date+"/"+b_month+"/"+b_year,"%d/%m/%Y")
#   print birth
    now = datetime.datetime.now()
#   print now
    print "===== Info ====="
    print "Birth date:", birth.strftime("%d/%m/%Y")
    print "Age:",int(now.year)-int(b_year)
    print "Years ago:",now-birth
birthDate()