
print"Calculator"



def calculator():

    input_1 = input("Enter Input 1 :")
    switch = True
    st_run = True
    while switch:

        #input_1 = input("Enter Input 1 :")

        operand = raw_input("Enter Operator :")
        input_2 = input("Enter Input 2 :")

        if operand.lower() == "clear" or operand.lower() == "c": #Recursive // Clear Case
            calculator()

        if operand.lower() != "exit" or input_1.lower() != "exit" or input_2.lower() != "exit":

            if operand == "+" or operand.lower() == "plus":  #PLUS Process

                if st_run == False:
                    result = p_sum+input_2
                    print "%d + %d = %d" % (p_sum, input_2, result)
                    p_sum = result

                elif st_run == True:
                    result = input_1 + input_2
                    p_sum = result
                    print "%d + %d = %d" % (input_1, input_2, result)
                    st_run = False

            elif operand == "-" or operand.lower() == "sub":  #SUB Process
                if st_run == False:
                    result = p_sum - input_2
                    print "%d - %d = %d" % (p_sum, input_2, result)
                    p_sum = result
                elif st_run == True:
                    result = input_1 - input_2
                    p_sum = result
                    print "%d - %d = %d" % (input_1, input_2, result)
                    st_run = False

            elif operand.lower() == "x" or operand.lower() == "mul":  #MULTI Process
                if st_run == False:
                    result = p_sum * input_2
                    print "%d x %d = %d" % (p_sum, input_2, result)
                    p_sum = result

                elif st_run == True:
                    result = input_1 * input_2
                    p_sum = result
                    print "%d x %d = %d" % (input_1, input_2, result)
                    st_run = False

            elif operand == "/" or operand.lower() == "divide":  #DIVIDE Process
                if st_run == False:
                    result = (p_sum*1.0) / input_2
                    print "%d / %d = %f" % (p_sum, input_2, result)
                    p_sum = result

                elif st_run == True:
                    result = (input_1*1.0) / input_2
                    p_sum = result
                    print "%d / %d = %f" % (input_1, input_2, result)
                    st_run = False


            elif operand == "%" or operand.lower() == "mod":  # MOD Process

                if st_run == False:
                    result = p_sum % input_2
                    print "%d / %d = %d" % (p_sum, input_2, result)
                    p_sum = result

                elif st_run == True:
                    result = input_1 % input_2
                    print "%d / %d = %d" % (input_1, input_2, result)
                    p_sum = result
                    st_run = False

            else:
                print "Wrong Operator"
        else:
            switch = False
            print ("Calculator End")
            exit()


#####Function##### not used
def plusFunction ():
    result = p_sum + input_2
    print  "%d + %d = %d" %(p_sum, num, result)
    return result

def subFunction ():
    result = p_sum - input_2
    print  "%d - %d = %d" %(p_sum, num, result)
    return result

def mulFunction ():
    result = p_sum * input_2
    print  "%d x %d = %d" %(p_sum, num, result)
    return result

def divFunction ():
    result = p_sum / input_2
    print  "%d / %d = %d" %(p_sum, num, result)
    return  result

def modFuntion ():
    result = p_sum % input_2
    print  "%d mod %d = %d" %(p_sum, num, result)
    return result

calculator()