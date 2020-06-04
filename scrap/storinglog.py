import mysql.connector
import datetime
def save(gvars):
	mydb = mysql.connector.connect(
	  host="localhost",
	  user=os.getenv("dbuser"),
	  passwd=os.getenv("dbpass"),
	  database="maillogs"
	)
	mycursor = mydb.cursor()
	ontime = str(datetime.datetime.now())	
	times = gvars[0]
	mail = gvars[1]
	mbody = gvars[2]
	sleep = gvars[3]
	sql = "INSERT INTO sentmails values( %s, %s, %s, %s, %s)"
	val = (ontime,mail,mbody,times,sleep)
	try :
		mycursor.execute(sql, val)
		mydb.commit()
		return ('saved')
	except:
		return ('notsaved')