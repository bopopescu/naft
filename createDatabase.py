import mysql.connector


#mydb = mysql.connector.connect(
    # host="localhost",
    # user="root",
    # passwd="",
    # database="gas"
# )

#mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE gas")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gas"
)

mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE gostare (id INTEGER AUTO_INCREMENT PRIMARY key,name VARCHAR(255))")
#mycursor.execute("CREATE TABLE gostare_pishraft (id INTEGER AUTO_INCREMENT PRIMARY key , gostare_id INTEGER(10) , darsad VARCHAR(255) , tarikh VARCHAR(255))")
#mycursor.execute("CREATE TABLE peymankaran (id INTEGER AUTO_INCREMENT PRIMARY key , check_id INTEGER(10) , check_money INTEGER (255) , tarikh VARCHAR(255) , tozihat VARCHAR(255)) ")
#mycursor.execute("CREATE TABLE  pipelinesF (id INTEGER AUTO_INCREMENT PRIMARY key , tarikh VARCHAR (255) , zekhamat VARCHAR (255) , metraj VARCHAR (255) , tonaj VARCHAR (255),tarikhTahvil VARCHAR (255),typeKalaTahvili VARCHAR (255) , shomareHavaleAnbar VARCHAR (255) , shomareTaghaza VARCHAR(255), shomareGhalam VARCHAR (255) , nerkhTashilBankMarkazi VARCHAR (255) , hazineAnbar VARCHAR (255), hazineSodoor VARCHAR (255) , hazineBime VARCHAR (255) ) ")
#mycursor.execute("CREATE TABLE arazi (id INTEGER AUTO_INCREMENT PRIMARY KEY , type VARCHAR (255) , date VARCHAR(255) , money VARCHAR(255))")
#mycursor.execute("CREATE TABLE pardakht_naftanir (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR (255) , sharh VARCHAR(255) , riyal VARCHAR(255) ,dollar VARCHAR(255) , peyvast_address VARCHAR (512),tozihat VARCHAR (255) , softDelete  VARCHAR (255))")
mycursor.execute("CREATE TABLE pardakht_gas (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR (255) , sharh VARCHAR(255) , riyal VARCHAR(255) ,dollar VARCHAR(255) , peyvast_address VARCHAR (512),tozihat VARCHAR (255) , softDelete  VARCHAR (255))")
