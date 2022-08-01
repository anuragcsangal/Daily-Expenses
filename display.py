import mysql.connector
from tabulate import tabulate
import db.py
import table.py
 

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database=database
              )

mycursor = mydb.cursor()
mycursor.execute(f"SELECT * FROM {table
        }")
myresult = mycursor.fetchall()


print(tabulate(myresult, headers=['Date','today','morning','afternoon','night','extras'], tablefmt='psql'))
