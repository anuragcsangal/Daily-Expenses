import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="DailyExpenses"
)

cursor = db.cursor()

morning = int(input("Enter morning expenses: "))
afternoon = int(input("Enter afternoon expenses: "))
night = int(input("Enter night expenses: "))
extras = int(input("Enter extras: "))

cursor.execute(f'''
        insert into userName(today, morning, afternoon, night, extras) values(current_date(), %s, %s, %s, %s)''', (morning, afternoon, night, extras))

db.commit()

