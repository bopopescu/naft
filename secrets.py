import os
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gas"
)

mycursor = mydb.cursor(buffered=True)
dirname = os.path.dirname(__file__)