
a = input("Enter Your Number:")

def multi(a):
    for i in range(1,13):
        result = a*i
        print "%d x %d = %d" %(a,i,result)

multi(a)