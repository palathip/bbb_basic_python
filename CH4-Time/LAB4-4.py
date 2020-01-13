data =\
"Interface IP-Address OK? Method Status Protocol\n"\
"GigabitEthernet1 192.168.1.3 YES manual down up\n"\
"GigabitEthernet2 172.17.111.3 YES manual up up\n"\
"GigabitEthernet3 192.168.101.3 YES manual up up"

# print data

list_data = data.splitlines()
# print list_data

for i in range(len(list_data)):
#    print list_data[i].split()
    if list_data[i].split()[4] == "down":
        print "WARNING :",list_data[i].split()[0],"(",list_data[i].split()[1],")","is",list_data[i].split()[4]

