import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",
                database="DailyExpenses"
              )

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM userName")
myresult = mycursor.fetchall()


print(tabulate(myresult, headers=['No','today','morning','afternoon','night','extras'], tablefmt='psql'))
