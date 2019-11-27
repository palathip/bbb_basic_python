
####LIST####
#list_fruit = ["apple","banana","cherry"]
#print list_fruit
#list_fruit.append("mango")
#print list_fruit
#print len(list_fruit)
#list_fruit[1] = "plum"
#print list_fruit

#Exercise
#LIST
print "\n LIST"
list_fruit = ["apple","banana","cherry","mengo"]
print list_fruit[2]
list_fruit.append("orange")
list_fruit.append("coconut")
print list_fruit
list_fruit[0] = "football"
print list_fruit
list_fruit.remove("banana")
print list_fruit
print len(list_fruit)

for fruit in list_fruit:
    print fruit

#Dictionary
#syntax
#.key
#

my_dict = {
    "date": 3,
    "month":"December",
    "year":2018
}

print "\nExample Dictionary"
print my_dict
my_dict["day"] = "monday"
print my_dict.keys()
print my_dict.values()
del my_dict["month"]
print my_dict

for x in my_dict:
    print x

for item in my_dict.values():
    print item


#Exersice Dictionary
print "\nEXERCISE DICTIONARY"
car = {
    "brand" :   "ford",
    "model" :   "Mustang",
    "year"  :   1964
       }
car["color"] = "rainbow"
print car
print car["model"]
print len(car)

#Exercise

print "\nALICE BOB EXERCISE"
list_name   = ["Alice","Bob","Oscar","Alice","Alice","Bob","Oscar","Bob"]
list_money  = [100,200,150,50,80,120,30,180]
merge = zip(list_name,list_money)

#SOLUTION 1
alicebob_dict1 = {}
for key,value in merge:
    if key in alicebob_dict1:
        alicebob_dict1[key] += value
    else:
        alicebob_dict1[key] = value
print "solution 1 zip"
print alicebob_dict1

#SOLUTION 2
alicebob_dict2 = {}
for count in range(len(list_name)):
    if alicebob_dict2.has_key(list_name[count]) == True:
        alicebob_dict2[list_name[count]] += list_money[count]
    else:
        alicebob_dict2[list_name[count]] = list_money[count]
print "\n solution 2 has key check"
print alicebob_dict2

#SOLUTION 3
alicebob_dict3 = {}
for i in range(len(list_name))
    if not list_name[i]