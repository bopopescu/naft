import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE gas CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="gas",
    # charset='utf8_persian_ci',use_unicode=True
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE gostare (id INTEGER AUTO_INCREMENT PRIMARY key,name VARCHAR(255),percent VARCHAR (255))")
mycursor.execute("CREATE TABLE gostare_pishraft (id INTEGER AUTO_INCREMENT PRIMARY key , gostare_id INTEGER(10) , darsad VARCHAR(255) , tarikh VARCHAR(255))")
mycursor.execute("CREATE TABLE peymankaran (id INTEGER AUTO_INCREMENT PRIMARY key,peymankar_name VARCHAR(255) , check_id INTEGER(10) , check_money INTEGER (255) , tarikh VARCHAR(255) , tozihat VARCHAR(255)) ")
mycursor.execute("CREATE TABLE  pipelinesF (id INTEGER AUTO_INCREMENT PRIMARY key  , zekhamat VARCHAR (255) , metraj VARCHAR (255) , tonaj VARCHAR (255),tarikhTahvil VARCHAR (255),typeKalaTahvili VARCHAR (255) , shomareHavaleAnbar VARCHAR (255) , shomareTaghaza VARCHAR(255), shomareGhalam VARCHAR (255) , nerkhTashilBankMarkazi VARCHAR (255) , hazineAnbar VARCHAR (255), hazineSodoorBime VARCHAR (255) ) ")
mycursor.execute("CREATE TABLE arazi (id INTEGER AUTO_INCREMENT PRIMARY KEY , sharh VARCHAR (255) , mablaghe_darkhasti_naftanir VARCHAR(255) , mablaghe_hoghooghi VARCHAR(255),tarikh_hoghooghi VARCHAR(255),mablaghe_taeed_mali VARCHAR(255),tarikh_taeed_omoor_mali VARCHAR(255),tarikh VARCHAR(255) , peyvast VARCHAR (255))")
mycursor.execute("CREATE TABLE pardakht_naftanir (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR (255) , sharh VARCHAR(255) , riyal VARCHAR(255),peyvast_address VARCHAR(255),dollar VARCHAR(255),tozihat VARCHAR (255) , softDelete  VARCHAR (255))")
mycursor.execute("CREATE TABLE pardakht_gas (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR (255) , sharh VARCHAR(255) , riyal VARCHAR(255) ,dollar VARCHAR(255) , peyvast_address VARCHAR (512),tozihat VARCHAR (255) , softDelete  VARCHAR (255))")
mycursor.execute("CREATE TABLE comper (id INTEGER AUTO_INCREMENT PRIMARY key , name VARCHAR(255),type VARCHAR(255) , dollar VARCHAR(255) , euro VARCHAR(255) , nerkh_dollar VARCHAR(255) , nerkh_euro VARCHAR(255) , tarikh_shoroo_tahvil VARCHAR(255) , tarikh_pardakht VARCHAR(255) ,tozihat VARCHAR(255)CHARACTER SET utf8 COLLATE utf8_general_ci )")
mycursor.execute("CREATE TABLE pardakht_shode_tavasote_naftanir_TM (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR(255), mablagh VARCHAR(255), pardakht_shod_babate VARCHAR(255),shomare_sanad VARCHAR(255),tozihat VARCHAR(255),softDelete VARCHAR(255))")
mycursor.execute("CREATE TABLE kala_30_inch (id INTEGER AUTO_INCREMENT PRIMARY key , estelam_1 VARCHAR(255) , estelam_2 VARCHAR(255) , estelam_3 VARCHAR(255))")
mycursor.execute("CREATE TABLE sadid_mahshahr ( money varchar(255), tik varchar(255) , tarikh VARCHAR (255))")
