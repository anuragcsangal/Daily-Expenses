import mysql.connector


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="Daily-Expenses"
)

cursor = db.cursor()


cursor.execute(f"create table de(today date , morning int, afternoon int, night int, extras int )")
