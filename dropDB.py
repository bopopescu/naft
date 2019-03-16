import DB as db

db.mycursor.execute("DROP DATABASE gas")
db.mydb.commit()