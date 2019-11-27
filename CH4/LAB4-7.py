# -*- coding: utf-8 -*-
switch = True
Out = ""
while switch:

    if Out.lower() != "y":
        try:
            mass = input("Mass:")
            volume = input("Volume:")
            result = float(mass) / float(volume)
            print "Density :",result

        except ZeroDivisionError:
            print "ERROR: ไม่สามารถหารด้วย 0 ได้"

        except NameError:
            print "ERROR: ไม่สามารถใส่ตัวอักษรได้"

        finally:
            Out = raw_input("ต้องการออกจากโปรแกรมหรือไม่(y):")
    else:
        switch = False
