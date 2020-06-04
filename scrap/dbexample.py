import mysql.connector
import datetime

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="tiger",
  database="maillogs"
)
mycursor = mydb.cursor()
ontime = now.strftime("%Y-%m-%d %H:%M:%S")
gvars = [4,"hhhhh@","hello","9sec"]
times = gvars[0]
mail = gvars[1]
mbody = gvars[2]
sleep = gvars[3]
#mycursor.execute
print("insert into sentmails values('"+ontime+"','"+mail+"','"+mbody+"','"+times+"','"+sleep+ "');")


now = datetime.datetime.now()
print ("Current date and time : ")
print ()

#print(mycursor.execute("insert into "))