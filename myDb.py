import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    passwd = "Wzh19960319!"
)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE dcrmdatabase")

print("All done!")