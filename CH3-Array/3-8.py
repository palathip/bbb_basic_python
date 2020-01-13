raw_data = [
{'salary': 8297, 'first_name': 'Richard', 'last_name': 'Alexander', 'gender': 'Male', 'age': 20, 'occupation': 'Fine Artist'},
{'salary': 1883, 'first_name': 'Rebecca', 'last_name': 'Adams', 'gender': 'Female', 'age': 26, 'occupation': 'Chef'},
{'salary': 588, 'first_name': 'Fenton', 'last_name': 'Perkins', 'gender': 'Male', 'age': 21, 'occupation': 'Driver'},
{'salary': 9381, 'first_name': 'Nicholas', 'last_name': 'Bailey', 'gender': 'Male', 'age': 23, 'occupation': 'Agronomist'},
{'salary': 2037, 'first_name': 'Ada', 'last_name': 'Adams', 'gender': 'Female', 'age': 23, 'occupation': 'Medic'},
{'salary': 5625, 'first_name': 'Dainton', 'last_name': 'Reed', 'gender': 'Male', 'age': 26, 'occupation': 'Archeologist'},
{'salary': 3009, 'first_name': 'Darcy', 'last_name': 'Moore', 'gender': 'Female', 'age': 28, 'occupation': 'Producer'},
{'salary': 1824, 'first_name': 'Myra', 'last_name': 'Russell', 'gender': 'Female', 'age': 21, 'occupation': 'Firefighter'},
{'salary': 3331, 'first_name': 'Sawyer', 'last_name': 'Davis', 'gender': 'Male', 'age': 22, 'occupation': 'Chemist'},
{'salary': 2022, 'first_name': 'Alina', 'last_name': 'Douglas', 'gender': 'Female', 'age': 26, 'occupation': 'Veterinarian'},
{'salary': 7595, 'first_name': 'Alen', 'last_name': 'Wright', 'gender': 'Male', 'age': 18, 'occupation': 'Carpenter'},
{'salary': 2552, 'first_name': 'Elise', 'last_name': 'Ellis', 'gender': 'Female', 'age': 25, 'occupation': 'Singer'},
{'salary': 9270, 'first_name': 'Vincent', 'last_name': 'Morgan', 'gender': 'Male', 'age': 28, 'occupation': 'Electrician'},
{'salary': 2742, 'first_name': 'Aldus', 'last_name': 'Harper', 'gender': 'Male', 'age': 28, 'occupation': 'Medic'},
{'salary': 2661, 'first_name': 'Roland', 'last_name': 'Fowler', 'gender': 'Male', 'age': 29, 'occupation': 'Actor'},
{'salary': 1490, 'first_name': 'Alan', 'last_name': 'Henderson', 'gender': 'Male', 'age': 30, 'occupation': 'Dancer'},
{'salary': 6212, 'first_name': 'Alfred', 'last_name': 'Murphy', 'gender': 'Male', 'age': 18, 'occupation': 'Lawer'},
{'salary': 3159, 'first_name': 'Carlos', 'last_name': 'Perry', 'gender': 'Male', 'age': 21, 'occupation': 'Lecturer'},
{'salary': 6913, 'first_name': 'Adelaide', 'last_name': 'Carroll', 'gender': 'Female', 'age': 25, 'occupation': 'Actor'},
{'salary': 931, 'first_name': 'Vanessa', 'last_name': 'Bailey', 'gender': 'Female', 'age': 20, 'occupation': 'Archeologist'}
]

#print raw_data[0]["salary"]
list_salary = []
for ind in range(len(raw_data)):
     #print raw_data[ind]["Salary"]
     list_salary.append(raw_data[ind]["salary"])

list_salary_age = []
for inde in  range(len(raw_data)):
     list_salary_age.append(raw_data[inde]["age"])

#print list_salary_age
#print sum(list_salary)


def totalSalary():
    sum_salary = 0
    for i in range(len(raw_data)):
            sum_salary = sum_salary + raw_data[i]["salary"]
    return sum_salary

def totalAge():
    sum_age = 0
    for i in range(len(raw_data)):
        sum_age = sum_age + raw_data[i]["age"]
    return sum_age

def countMale():
    count = 0
    for i in range(len(raw_data)):
        if raw_data[i]["gender"] == "Male":
            count += 1
    return count

def countFemale():
    count = 0
    for i in range(len(raw_data)):
        if raw_data[i]["gender"] == "Female":
            count += 1
    return count

def info(index):
    print "Name:",raw_data[index]["first_name"],raw_data[index]["last_name"]
    print "Gender:",raw_data[index]["gender"]
    print "Age:", raw_data[index]["age"]
    print "Occupation:", raw_data[index]["occupation"]
    print "Salary:", raw_data[index]["salary"]

print "====SUMMARY===="
print "Total Employees :",len(raw_data)
print "Total Salary :",totalSalary(),"$"
print "Average Salary : %.2f $" %(totalSalary()*1.0/len(raw_data))
print "Average Age %d" %(totalAge()*1.0/len(raw_data))
print "Total Male :" ,countMale()
print "Total Female",countFemale()
print "==============="
print "Maximum Salary"
index = list_salary.index(max(list_salary))
info(index)
print "\nMinimum Salary"
index = list_salary.index(min(list_salary))
info(index)
print "==============="
print "Maximum Age"
index = list_salary_age.index(max(list_salary_age))
info(index)
print "\nMinimum Age"
index = list_salary_age.index(min(list_salary_age))
info(index)



max_salary_index = list_salary.index(max(list_salary))



