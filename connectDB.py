import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "test"
)
if mydb:
    print "Success"

else:
    print "Fail"

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM bbb")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
