# -*- coding: utf-8 -*-

#### FOR LOOP ####
word = raw_input("INPUT:")
def loop_range():
    for x in word:
        print x

loop_range(word)











##### WHILE LOOP #####
#if exit == ออก
#Condition for exit while loop

def sol1(): #interrapt while solution 1
    while raw_input("Enter Someting :") != 'exit':
        print "hello"

def sol2(): #interrapt while solution 2
    switch = True
    while switch:
        text = raw_input("Enter something")
        if text.lower() != "exit":
            print "hello"
        else:
            switch = False


#Exercise of While Loop
#Check Odd & Even Number

def checkNumber2v(): # 2 Varible
    switch = True
    while switch:
        number = raw_input("Enter something:")
        if number.lower() != "exit":
            if int(number)%2 == 0:
                print "even"
            else:
                print "odd"
        else:
            switch = False
    print ("End")

#checkNumber2v()

def checkNumber1v(): # 1 Variable
    number = True
    while number:
        number = raw_input("Enter something:")
        if number.lower() != "exit":
            if int(number)%2 == 0:
                print "even"
                number = True
            else:
                print "odd"
                number = True
        else:
            number = False
    print ("End")

#checkNumber1v()
