import mysql.connector as mcnx
import pandas as pd

mydb = mcnx.connect(
    database="classicmodels",
    user="root",
    password="root"
)

cursor = mydb.cursor()
cursor.execute("select * from customers")
result = cursor.fetchall()

df = pd.DataFrame(result, columns=list(cursor.column_names))

print("hello")

