import mysql.connector
from tabulate import tabulate
 

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="Daily-Expenses"
              )

mycursor = mydb.cursor()
mycursor.execute(f"SELECT * FROM de")
myresult = mycursor.fetchall()


print(tabulate(myresult, headers=['Date','today','morning','afternoon','night','extras'], tablefmt='psql'))
