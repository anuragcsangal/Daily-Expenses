import mysql.connector
import db.py
import table.py

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database=database
)

cursor = db.cursor()

morning = int(input("Enter morning expenses: "))
afternoon = int(input("Enter afternoon expenses: "))
night = int(input("Enter night expenses: "))
extras = int(input("Enter extras: "))

cursor.execute(f'''
        insert into {table}(today, morning, afternoon, night, extras) values(current_date(), %s, %s, %s, %s)''', (morning, afternoon, night, extras))

db.commit()

