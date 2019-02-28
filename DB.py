import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gas"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE gostare (id INTEGER AUTO_INCREMENT PRIMARY key,name VARCHAR(255))")
# mycursor.execute("SHOW TABLES")
# for table in mycursor:
#     print(table)


# sqlStuff = "INSERT INTO gostare (name) value (%s)"
# record = ("ahwaz",)
#
# mycursor.execute(sqlStuff , record)
# mydb.commit()


#
# sqlStuff = "INSERT INTO gostare_pishraft (gostare_id , darsad , tarikh) VALUES (%s , %s ,%s)"
# record = ("1",
#           "20",
#           "20/18/79",
#           )
#
# mycursor.execute(sqlStuff,record)
# mydb.commit()
