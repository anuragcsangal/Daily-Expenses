import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        )

cursor = db.cursor()

database = input("Enter Database Name: ")

cursor.execute(f"create database {database}")


