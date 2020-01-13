

def addAvenger():

    avenger = []
    switch = True
    while switch:
        name = raw_input("Enter Name to Avenger Team:")
        if name.lower() != "exit":
            avenger.append(name)
            print "===My Team==="
            for i in range(len(avenger)):
                print i + 1, '.', avenger[i]
            print "============="

        else:
            switch = False
    print ("End")
addAvenger()