import mysql.connector
import pandas
#
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
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE gostare (id INTEGER AUTO_INCREMENT PRIMARY key,name VARCHAR(255),percent VARCHAR (255) , tarikh VARCHAR (255))")
mycursor.execute("CREATE TABLE gostare_pishraft (id INTEGER AUTO_INCREMENT PRIMARY key , gostare_id INTEGER(10) , darsad VARCHAR(255) , tarikh VARCHAR(255) ,id_ghest VARCHAR (255) , tozihat VARCHAR (255) , malg BOOLEAN)")
mycursor.execute("CREATE TABLE peymankaran (id INTEGER AUTO_INCREMENT PRIMARY key,peymankar_name VARCHAR(255) , check_id INTEGER(10) , check_money VARCHAR (255) , tarikh VARCHAR(255) , tozihat VARCHAR(255)) ")
mycursor.execute("CREATE TABLE pipelinesF (id INTEGER AUTO_INCREMENT PRIMARY key  , zekhamat VARCHAR (255) , metraj VARCHAR (255) , tonaj VARCHAR (255),tarikhTahvil VARCHAR (255),typeKalaTahvili VARCHAR (255) , shomareHavaleAnbar VARCHAR (255) , shomareTaghaza VARCHAR(255), shomareGhalam VARCHAR (255) , nerkhTashilBankMarkazi VARCHAR (255) , hazineAnbar VARCHAR (255), hazineSodoorBime VARCHAR (255) , se VARCHAR (255) ,tarikh VARCHAR (255) , adam_ghatiyat VARCHAR (255)) ")
mycursor.execute("CREATE TABLE arazi (id INTEGER AUTO_INCREMENT PRIMARY KEY , sharh VARCHAR (255) , mablaghe_darkhasti_naftanir VARCHAR(255) , mablaghe_hoghooghi VARCHAR(255),tarikh_hoghooghi VARCHAR(255),mablaghe_taeed_mali VARCHAR(255),tarikh_taeed_omoor_mali VARCHAR(255),tarikh VARCHAR(255) , peyvast VARCHAR (255))")
mycursor.execute("CREATE TABLE pardakht_naftanir (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR (255) , sharh VARCHAR(255) , riyal VARCHAR(255),peyvast_address VARCHAR(255),dollar VARCHAR(255),tozihat VARCHAR (255) , softDelete  VARCHAR (255))")
mycursor.execute("CREATE TABLE pardakht_gas (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR (255) , sharh VARCHAR(255) , riyal VARCHAR(255) ,dollar VARCHAR(255) , peyvast_address VARCHAR (512),tozihat VARCHAR (255) , softDelete  VARCHAR (255))")
mycursor.execute("CREATE TABLE comper (id INTEGER AUTO_INCREMENT PRIMARY key , name VARCHAR(255),type VARCHAR(255) , dollar VARCHAR(255) , euro VARCHAR(255) , nerkh_dollar VARCHAR(255) , nerkh_euro VARCHAR(255) , tarikh_shoroo_tahvil VARCHAR(255) , tarikh_pardakht VARCHAR(255) ,tozihat VARCHAR(255), peyvast VARCHAR (255))")
mycursor.execute("CREATE TABLE pardakht_shode_tavasote_naftanir_TM (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR(255), mablagh VARCHAR(255), pardakht_shod_babate VARCHAR(255),shomare_sanad VARCHAR(255),tozihat VARCHAR(255),state VARCHAR (255),softDelete VARCHAR(255))")
mycursor.execute("CREATE TABLE kala_30_inch (id INTEGER AUTO_INCREMENT PRIMARY key , estelam_1 VARCHAR(255) , estelam_2 VARCHAR(255) , estelam_3 VARCHAR(255))")
mycursor.execute("CREATE TABLE sadid_mahshahr (id INTEGER AUTO_INCREMENT PRIMARY key, money varchar(255), asl_dar_mohasebat varchar(255) , tarikh VARCHAR (255) , jarime VARCHAR (255))")
mycursor.execute("CREATE TABLE jadval56 (id INTEGER AUTO_INCREMENT PRIMARY key, pool varchar(255), tarikh VARCHAR (255) , ekhtelaf INTEGER (255) , sharh VARCHAR (255))")
mycursor.execute("CREATE TABLE naftanir_peymankaran_adam (id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR(255), mablagh VARCHAR(255), pardakht_shod_babate VARCHAR(255),shomare_sanad VARCHAR(255),tozihat VARCHAR(255),state VARCHAR (255),softDelete VARCHAR(255))")

mycursor.execute("CREATE TABLE jarime_taakhir_dar_pardakht (id INTEGER AUTO_INCREMENT PRIMARY KEY , shomare_pardakht_be_taakhir_oftade VARCHAR(255), mablagh_pardakht VARCHAR(255), tarikh_barname_pardakht VARCHAR(255),tarikh_jadid_pardakht VARCHAR(255) , file_peyvast VARCHAR(255) , mohasebe_takhir VARCHAR (255) , mizan_takhir VARCHAR (255) , jarime VARCHAR (255) , mizane_taakhir_dar_mohasebat_ghest VARCHAR (255))")
mycursor.execute("CREATE TABLE taahodat_pardakht_sherkat_mohandesi_tose_gas(id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR(255), sharh VARCHAR(255), mablagh_dollari VARCHAR(255),tozihat VARCHAR(255),file_peyvast VARCHAR(255))")
mycursor.execute("CREATE TABLE taahodat_pardakht_sherkat_naftanir(id INTEGER AUTO_INCREMENT PRIMARY KEY , tarikh VARCHAR(255), sharh VARCHAR(255), mablagh_dollari VARCHAR(255),tozihat VARCHAR(255),file_peyvast VARCHAR(255))")


mycursor.execute("CREATE TABLE taakhir_dar_bahre_bardari (id  INTEGER AUTO_INCREMENT PRIMARY KEY ,gostare_id VARCHAR (255) , darsad VARCHAR (255) , tarikh_ghest_avaliye VARCHAR (255), tarikh_ghest_jariye VARCHAR (255),shomare_ghest VARCHAR (255) , javab VARCHAR (255))")
mydb.commit()
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("ahwaz" , "15.95" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("koohdasht" , "14.10" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("bestoon" , "15.10" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("dezfool" , "16.83" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("kermanshah" , "1.75" ,"1396-2-12"))
# mycursor.execute("insert into gostare (name , percent , tarikh) values (koohdasht , 14.10 , 1396-2-12)")
# mycursor.execute("insert into gostare (name , percent , tarikh) values (bestoon , 15.10 , 1396-2-12)")
# mycursor.execute("insert into gostare (name , percent , tarikh) values (dezfool , 16.83 , 1396-2-12)")
# mycursor.execute("insert into gostare (name , percent , tarikh) values (kermanshah , 1.75 , 1396-2-12)")

mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("feshar_ahwaz" , "7.69" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("feshar_hoseiniye" , "7.69" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("feshar_koohdasht" , "6.69" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("feshar_deylam" , "6.69" ,"1396-2-12"))
mycursor.execute("insert into gostare (name , percent , tarikh) values (%s , %s , %s)", ("feshar_bidboland" , "6.69" ,"1396-2-12"))

# mycursor.execute("insert into gostare (name , percent , tarikh) values (feshar_ahwaz , 7.69 , 1397-2-12)")
# mycursor.execute("insert into gostare (name , percent , tarikh) values (feshar_hoseiniye , 7.69 , 1397-2-12)")
# mycursor.execute("insert into gostare (name , percent , tarikh) values (feshar_koohdasht , 6.96 , 1397-2-12)")
# mycursor.execute("insert into gostare (name , percent , tarikh) values (feshar_deylam , 6.96 , 1397-2-12)")
# mycursor.execute("insert into gostare (name , percent , tarikh) values (feshar_bidboland , 6.96 , 1397-2-12)")


# mycursor.execute("CREATE TABLE model_mali (id INTEGER AUTO_INCREMENT PRIMARY KEY ,aghsat_marboot_be_taasisat_feshar VARCHAR(255),aghsat_marboot_be_khotoot VARCHAR(255),vazne mali VARCHAR(255) ,0 VARCHAR(255) , 1 VARCHAR(255) ,2 VARCHAR(255) ,3 VARCHAR(255) ,4 VARCHAR(255) , 5 VARCHAR(255) , 6 VARCHAR(255) , 7 VARCHAR(255) , 8 VARCHAR(255) , 9 VARCHAR(255) ,10 VARCHAR(255))")

mydb.commit()
#
# model_mali_csv = pandas.read_csv('model_mali.csv')
# print (type(model_mali_csv))
# df = pandas.DataFrame(model_mali_csv)
# i = 0
# while i < 30:
#     s = df.iloc[[i]].values.tolist()
#     s = tuple(s[0])
#     print(s)
#     i += 1