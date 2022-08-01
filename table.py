import mysql.connector
import db.py 


db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database=database
)

cursor = db.cursor()

table = input("Enter Table Name: ")

cursor.execute(f"create table {table}(today date , morning int, afternoon int, night int, extras int )")

