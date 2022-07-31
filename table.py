import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="DailyExpenses"
)

cursor = db.cursor()

cursor.execute("create table userName(today date , morning int, afternoon int, night int, extras int )")

