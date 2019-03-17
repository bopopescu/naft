import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)
import DB as db
import mysql.connector
import json

class gostare(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_gostare')
        args = parser.parse_args()
        if args['id_gostare']:
            db.mycursor.execute("SELECT * FROM gostare_pishraft WHERE gostare_id =%s ",(args['id_gostare'],))
            pihraft_with_id = db.mycursor.fetchall()
            return pihraft_with_id
        db.mycursor.execute("""SELECT * FROM gostare""")
        gostare = db.mycursor.fetchall()
        db.mycursor.execute("""SELECT * FROM gostare_pishraft""")
        pishraft = db.mycursor.fetchall()
        res= {}
        res["gostareha"] = gostare
        res["pishraft"] = pishraft
        return res


    def post(selfs):
        # json = request.get_json()
        # return {"you sent":json}, 201
        parser = reqparse.RequestParser()
        parser.add_argument('tarikh')
        parser.add_argument('darsade_bardari')
        parser.add_argument('mahe_khali')
        parser.add_argument('id_gostare')
        args = parser.parse_args()
        #if args['mahe_khali'] and args['id_gostare']:
            #values =  ( int(args['id_gostare']) ,0 ,args['mahe_khali'] ,)
            ## print(values)
            #db.mycursor.execute("INSERT INTO gostare_pishraft(gostare_id , darsad , tarikh) values (%s , %s , %s)", values)
            #db.mydb.commit()
            #return True

        if args['darsade_bardari'] and args['tarikh'] and args['id_gostare']:
            values = (args['id_gostare'],args['darsade_bardari'] , args['tarikh'] , )
            # print(values)
            db.mycursor.execute("INSERT INTO gostare_pishraft(gostare_id , darsad , tarikh) values (%s , %s , %s)", values)
            db.mydb.commit()
            return True
        return False

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_gostare')
        parser.add_argument('id_pishraft')
        args = parser.parse_args()
        if args['id_gostare']:
            db.mycursor.execute("DELETE FROM gostare WHERE id = %s" , (args['id_gostare'] ,))
            db.mycursor.execute("DELETE FROM gostare_pishraft WHERE gostare_id = %s",(args['id_gostare'],))
            db.mydb.commit()
            return "gostare deleted"
        if args['id_pishraft']:
            db.mycursor.execute("DELETE FROM gostare_pishraft where id = %s" , (args['id_pishraft'],))
            db.mydb.commit()
            return "pishraft deleted"

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('darsad')
        args = parser.parse_args()
        db.mycursor.execute("UPDATE gostare_pishraft SET darsad = %s WHERE id = %s " , (args['darsad'], args['id'],))
        db.mydb.commit()
        return "salam"
        

class peymankaran(Resource):
    def get(self):
        db.mycursor.execute("SELECT * FROM peymankaran")
        ret = db.mycursor.fetchall()
        return ret;
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('check_id')
        parser.add_argument('money')
        parser.add_argument('tarikh')
        parser.add_argument('tozih')
        parser.add_argument('name')

        args = parser.parse_args()
        db.mycursor.execute("INSERT INTO peymankaran (peymankar_name,check_id , check_money , tarikh , tozihat) VALUES (%s,%s , %s ,%s , %s)" , (args['name'],args['check_id'],args['money'],args['tarikh'] , args['tozih'] , ))
        db.mydb.commit()
        return True
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        args = parser.parse_args()
        db.mycursor.execute("DELETE FROM peymankaran WHERE id = %s " , (args['id'],))
        db.mydb.commit()
        return "delete"

class arazi(Resource):
    def get(self):
        db.mycursor.execute("SELECT * FROM arazi")
        ret = db.mycursor.fetchall()
        return ret
    def post(self):
        #//TODO: have to add peyvast FIles
        parser = reqparse.RequestParser()
        parser.add_argument("sharh")
        parser.add_argument("mablaghe_darkhasti_naftanir")
        parser.add_argument("mablaghe_hoghooghi")
        parser.add_argument("tarikh_hoghooghi")
        parser.add_argument("mablaghe_taeed_mali")
        parser.add_argument("tarikh_taeed_omoor_mali")
        parser.add_argument("stateDate")
        parser.add_argument("peyvast",type=werkzeug.datastructures.FileStorage,location = 'files')
        args = parser.parse_args()
        file = args['peyvast']
        if file:
            dirname = os.path.dirname(__file__)
            file.save(os.path.join(dirname,'files',file.filename))
            fileName = file.filename
        else:
            fileName = None
        sql = "INSERT INTO arazi (sharh , mablaghe_darkhasti_naftanir , mablaghe_hoghooghi,tarikh_hoghooghi ,mablaghe_taeed_mali ,tarikh_taeed_omoor_mali ,tarikh , peyvast) VALUES (%s , %s , %s, %s,%s,%s,%s,%s)"
        values = (args['sharh'] , args['mablaghe_darkhasti_naftanir'] , args['mablaghe_hoghooghi'] ,args['tarikh_hoghooghi'],args['mablaghe_taeed_mali'],args['tarikh_taeed_omoor_mali'],args['stateDate'],fileName)
        db.mycursor.execute(sql , values)
        db.mydb.commit()
        return True
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        args = parser.parse_args()
        db.mycursor.execute("DELETE FROM arazi WHERE id = %s " , (args['id'],))
        db.mydb.commit()
        return "delete"

    
class pipeLinesF(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('tarikh')
        parser.add_argument('zekhamat')
        parser.add_argument('metraj')
        parser.add_argument('tonaj')
        parser.add_argument('tarikhTahvil')
        parser.add_argument('typeKalaTahvili')
        parser.add_argument('shomareHavaleAnbar')
        parser.add_argument('shomareTaghaza')
        parser.add_argument('shomareGhalam')
        parser.add_argument('nerkhBank')
        parser.add_argument('hazineAnbar')
        parser.add_argument('hazineSodoorBime')
        parser.add_argument('hazineBime')
        parser.add_argument('36Inch')
        parser.add_argument('tarikh')
        args = parser.parse_args()
        
        # mysql = "INSERT INTO pipelinesf (tarikh ,zekhamat , metraj , tonaj , tarikhTahvil,typeKalaTahvil ,shomareHavaleAnbar , shomareTaghaza,shomareGhalam ,nerkhTashilBankMarkazi ,hazineAnbar , hazineSodoor, hazineBime , mablagheVaragh , avarezGomrok , hazineSakhteLoole , hazinePooshesh , maliatVaragh, maliatSakht )"
        mysql = "INSERT INTO pipelinesf (" \
                "zekhamat , " \
                "metraj , " \
                "tonaj , " \
                "tarikhTahvil," \
                "typeKalaTahvili ," \
                "shomareHavaleAnbar , " \
                "shomareTaghaza," \
                "shomareGhalam ," \
                "nerkhTashilBankMarkazi ," \
                "hazineAnbar , " \
                "hazineSodoorBime , se , tarikh) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s ,%s)"
        values = (
                  args['zekhamat'],
                  args['metraj'],
                  args['tonaj'],
                  args['tarikhTahvil'],
                  args['typeKalaTahvili'],
                  args['shomareHavaleAnbar'],
                  args['shomareTaghaza'],
                  args['shomareGhalam'],
                  args['nerkhBank'],
                  args['hazineAnbar'],
                  args['hazineSodoorBime'],
                  args['36Inch'],args['tarikh'])
        db.mycursor.execute(mysql ,values)
        db.mydb.commit()
        return True
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("36_inch")
        args = parser.parse_args()
        if args['36_inch']:
            db.mycursor.execute("SELECT * FROM pipelinesf WHERE se IS NOT NULL ")
        else:
            db.mycursor.execute("SELECT * FROM pipelinesf WHERE se IS NULL")
        data = db.mycursor.fetchall()
        ret = {}
        for record in data:
            mablaghe_varagh = int(record[3])*1033
            avarez_gomrok = mablaghe_varagh * int(record[9]) * 4/100
            maliyat_bar_arzesh_afzoode_varagh = avarez_gomrok * 1/10
            hazine_sakht_loole = 0
            if record[5] == "ورق" :
                hazine_sakht_loole = 0
            else :
                hazine_sakht_loole = int(record[3]) * 125
            hazine_pooshesh = 0
            if record[5] == "پوشش داده شده":
                hazine_pooshesh = int(record[3])*95
            maliyat_bar_arzesh_afzoode_sakht_pooshesh = (hazine_sakht_loole + hazine_pooshesh) *  int(record[9]) * 10/100
            motalebate_riyali = int(record[10]) + int(record[11]) + avarez_gomrok + maliyat_bar_arzesh_afzoode_varagh + maliyat_bar_arzesh_afzoode_sakht_pooshesh
            motalebat_arzi = hazine_pooshesh + hazine_sakht_loole

            ret[record[0]] ={'dataBase' : record ,
                             'mablaghe_varagh':mablaghe_varagh,
                             'avarez_gomrok':avarez_gomrok,
                             'maliyat_bar_arzesh_varagh':maliyat_bar_arzesh_afzoode_varagh,
                             'hazine_sakhte_loole':hazine_sakht_loole,
                             'hazine_pooshesh':hazine_pooshesh,
                             'maliyat_bara_arzesh_afzoode_sakhte_pooshesh':maliyat_bar_arzesh_afzoode_sakht_pooshesh,
                             'motalebat_riyali':motalebate_riyali,
                             'motalebat_arzi':motalebat_arzi}
        return ret

class pardakht_naftanir(Resource):
    def get(self):
        ret = {}
        db.mycursor.execute("SELECT * FROM pardakht_naftanir WHERE softDelete is NULL ")
        ready = db.mycursor.fetchall()
        db.mycursor.execute("SELECT * FROM pardakht_naftanir WHERE softDelete is NOT NULL ")
        softDeletes = db.mycursor.fetchall()
        ret['softDeletes'] = softDeletes
        ret['ready'] = ready
        return ret

    def post(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument("peyvast",type=werkzeug.datastructures.FileStorage)
        parser = reqparse.RequestParser()
        parser.add_argument("date")
        parser.add_argument("sharh")
        parser.add_argument("dollar")
        parser.add_argument("riyal")
        parser.add_argument("tozihat")
        parser.add_argument("peyvast",type=werkzeug.datastructures.FileStorage,location = 'files')
        args = parser.parse_args()
        file = args['peyvast']
        dirname = os.path.dirname(__file__)
        file.save(os.path.join(dirname,'files',file.filename))
        db.mycursor.execute("INSERT INTO pardakht_naftanir ( tarikh ,sharh , dollar , riyal, peyvast_address , tozihat ) VALUES (%s,%s,%s,%s,%s,%s)" ,
                            (args['date'],args['sharh'] , args['dollar'] , args['riyal'] , file.filename ,args['tozihat'], ))
        db.mydb.commit()

        return True
    #TODO: add update and delete
    #def delete(self):
        #parser = 

class pardakht_tose_gas(Resource):
    def get(self):
        ret = {}
        db.mycursor.execute("SELECT * FROM pardakht_gas WHERE softDelete is NULL ")
        ready = db.mycursor.fetchall()
        db.mycursor.execute("SELECT * FROM pardakht_gas WHERE softDelete is NOT NULL ")
        softDeletes = db.mycursor.fetchall()
        ret['softDeletes'] = softDeletes
        ret['ready'] = ready
        return ret
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("peyvast",type=werkzeug.datastructures.FileStorage,location = 'files')
        parser.add_argument("date")
        parser.add_argument("sharh")
        parser.add_argument("dollar")
        parser.add_argument("riyal")
        parser.add_argument("tozihat")
        args = parser.parse_args()
        file = args['peyvast']
        dirname = os.path.dirname(__file__)
        file.save(os.path.join(dirname,'files',file.filename))
        db.mycursor.execute("INSERT INTO pardakht_gas ( tarikh ,sharh , dollar , riyal, peyvast_address , tozihat ) VALUES (%s,%s,%s,%s,%s,%s)" ,
                            (args['date'],args['sharh'] , args['dollar'] , args['riyal'] , file.filename ,args['tozihat'], ))
        db.mydb.commit()


class comper(Resource):
    def get(self):
        db.mycursor.execute("SELECT * FROM comper")
        data = db.mycursor.fetchall()
        ret = {}
        for record in data:
            ret[record[0]] = {'dataBase': record ,
                              'natayej_motalebat': (int(record[4]) * (int(record[5])/int(record[6])))}
        return ret
    def post(self):
        parser = reqparse.RequestParser()
        #//TODO:: have to add peyvast file 
        parser.add_argument("name")
        parser.add_argument("type")
        parser.add_argument("dollar")
        parser.add_argument("euro")
        parser.add_argument("nerkh_dollar")
        parser.add_argument("nerkh_euro")
        parser.add_argument("tarikh_shoroo_tahvil")
        parser.add_argument("tarikh_pardakht")
        parser.add_argument("tozihat")
        parser.add_argument("peyvast",type=werkzeug.datastructures.FileStorage,location = 'files')
        args = parser.parse_args()
        file = args['peyvast']
        if file:
            dirname = os.path.dirname(__file__)
            file.save(os.path.join(dirname, 'files', file.filename))
            fileName = file.filename
        else:
            fileName = None
        db.mycursor.execute('INSERT INTO comper (name , type , dollar , euro , nerkh_dollar , nerkh_euro , tarikh_shoroo_tahvil , tarikh_pardakht , tozihat,peyvast) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                            (args['name'],args['type'],args['dollar'],args['euro'],args['nerkh_dollar'],args['nerkh_euro'],args['tarikh_shoroo_tahvil'],args['tarikh_pardakht'],args['tozihat'],fileName))
        db.mydb.commit()
        return True
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        args = parser.parse_args()
        db.mycursor.execute('DELETE FROM comper WHERE id = %s' , (args['id'],))
        db.mydb.commit()
        return True


#// taraz mali
class pardakht_shode_tavasote_naftanir(Resource):
    def get(self):
        db.mycursor.execute("SELECT * FROM pardakht_shode_tavasote_naftanir_tm ")
        ret = db.mycursor.fetchall()
        return ret
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("tarikh")
        parser.add_argument("mablagh")
        parser.add_argument("pardakht_shod_babate")
        parser.add_argument("shomare_sanad")
        parser.add_argument("tozihat")
        args = parser.parse_args()
        db.mycursor.execute("INSERT INTO pardakht_shode_tavasote_naftanir_tm (tarikh , mablagh , pardakht_shod_babate,shomare_sanad , tozihat) VALUES (%s,%s,%s,%s,%s)",
                            (args['tarikh'] , args['mablagh'],args['pardakht_shod_babate'],args['shomare_sanad'],args['tozihat'],))
        db.mydb.commit()
        return True
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("tarikh")
        args = parser.parse_args()
        if args['id'] and args['tarikh']:
            db.mycursor.execute("UPDATE pardakht_shode_tavasote_naftanir_tm SET softdelete = %s WHERE id = %s" , (args['id'] , args['tarikh'],))
            db.mydb.commit()
            return True
        if args['id']:
            db.mycursor.execute("DELETE FROM pardakht_shode_tavasote_naftanir_tm where id = %s" ,(args['id'],))
            db.mydb.commit()
            return True
        return False

class kala_30(Resource):
    def get(self):
        db.mycursor.execute("select * from kala_30_inch ")
        data = db.mycursor.fetchall()
        ret = {}
        # ret['miyangin']=(int(data[0][1])+int(data[0][2])+int(data[0][3])) / 3
        # ret['shandool']= "shandool"
        miyangin = {}
        # return data
        for record in data:
            ret['database_record'+str(record[0])] = int(record[1]),int(record[2]),int(record[3])
            ret['miyangin__'+str(record[0])] = (int(record[1]) + int(record[2]) + int(record[3])) / 3
            ret['maliayt__'+str(record[0])] = ((int(record[1]) + int(record[2]) + int(record[3])) / 3) * 1/10
        return ret
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('estelam1')
        parser.add_argument('estelam2')
        parser.add_argument('estelam3')
        args = parser.parse_args()
        db.mycursor.execute("INSERT INTO kala_30_inch (estelam_1 , estelam_2, estelam_3) VALUES (%s , %s ,%s )",
                            (args['estelam1'],args['estelam2'],args['estelam3'],))
        db.mydb.commit()
        return True

class sadid_mahshahr(Resource):
    def get(self):
        db.mycursor.execute("SELECT * FROM sadid_mahshahr")
        ret = db.mycursor.fetchall()
        return ret
    def post(self):
        db.mycursor.execute("SELECT * FROM sadid_mahshahr")
        DATA = db.mycursor.fetchall()
        for d in DATA:
            db.mycursor.execute("DELETE FROM sadid_mahshahr WHERE money = %s" ,(d[0],))
            db.mydb.commit()
        parse = reqparse.RequestParser()
        parse.add_argument("money")
        parse.add_argument("tik")
        parse.add_argument("tarikh")
        args = parse.parse_args()
        db.mycursor.execute("INSERT INTO sadid_mahshahr(money , tik)  VALUES(%s , %s) " , (args['money'] , args['tik'],args['tarikh']))
        return True
class jadval56(Resource):
    def get(self):
        p56 = pipeLinesF()
        p56 =  p56.get()
        p56 = json.dumps(p56)
        p56 = json.loads(p56)
        pipeline56 = {}
        for id in  p56:
             pipeline56[id] = {}
             pipeline56[id]['taahod_be_pardakht'] = p56[id]['motalebat_riyali']
             # jareme = jarime(1 ,1 ,1 ,1)
             pipeline56[id]['jarime'] = 1
             if int(id) == 1:
                pndg = 0
             else:
                pndg = pipeline56[str(int(id) - 1)]['kole_motalebat']
             pipeline56[id]['pardakht_nashode_dore_ghable'] = pndg
             pipeline56[id]['kole_motalebat'] = int(pipeline56[id]['jarime']) + pndg + pipeline56[id]['taahod_be_pardakht']
        return pipeline56
class jadvalArazi(Resource):
    def get(self):
        arz = arazi()
        arz = arz.get()
        arz = json.dumps(arz)
        arz = json.loads(arz)
        jarazi = {}
        for id in arz:
            jarazi[id] ={}
            jarazi[id]['pardakht_shode_tavasote_naftanir'] = arz[id][3]
            jarazi[id]['tarikh_taaid_hoghooghi'] = arz[id][3]
            jarazi[id]['taahod_be_pardakht_naftanir'] = 85747896194
            jarazi[id]['jame_kole_mohasebat'] = int(jarazi[id]['taahod_be_pardakht_naftanir']) - int(arz[id][3])
            jarazi[id]['jarime'] = "todo : havent add it"
        return jarazi

class looleSaziSadid(Resource):
    def get(self):
        sadid = sadid_mahshahr()
        sadid = sadid.get()
        ret = {}
        # ret['pardakht_shode_tavasote_naftanir'] = 0
        # ret['taahod_be_pardakht'] = int(sadid[0][0]) / 3
        # ret['pardakht_nashode_dore_ghabl'] = 0
        # ret['jarime_dore_ghable'] = 0
        # ret['kole_motalebat'] = int(ret['jarime_dore_ghable']) + int(ret['pardakht_nashode_dore_ghabl'])
        # return str(sadid[0][2])
        # return ret
        for i in range(3):
            ret[i] = {}
            ret[i]['tarikh'] = sadid[0][2]
            ret[i]['naftanir'] = 0
            ret[i]['taahod'] = int(sadid[0][0])/3
            if i == 0:
                ret[i]['dore_ghabl'] = 0
                ret[i]['jarime'] = 0
            else :
                ret[i]['dore_ghabl'] = ret[i-1]['kol']
                ret[i]['jarime'] = 1
            ret[i]['kol'] = ret[i]['jarime'] + int(ret[i]['dore_ghabl'] ) + int(sadid[0][0])/3
        return  ret
class jadvalPeymankaran(Resource):
    def get(self):
        return "bayad soal beshe hanooz kamel nist"
api.add_resource(gostare,"/gostare")
api.add_resource(comper,"/comperosor")
api.add_resource(peymankaran,"/peymankaran")
api.add_resource(pipeLinesF,"/pipeLinesF")
api.add_resource(arazi , "/arazi")
api.add_resource(pardakht_naftanir , "/pardakht_naftanir")
api.add_resource(pardakht_shode_tavasote_naftanir , "/pardakht_shode_tavasote_naftanir_TM")
api.add_resource(kala_30 , "/kala_30")
api.add_resource(sadid_mahshahr , "/sadid_mahshahr")
api.add_resource(jadval56 , "/jadval56")
api.add_resource(jadvalArazi , "/jadvalArazi")
api.add_resource(looleSaziSadid , "/jadval_loole_sazi_sadid")
api.add_resource(jadvalPeymankaran , "/jadval_peymankaran")
# import locale , jdatetime
from datetime import datetime , date
def jarime(dore_ghable , nerkh_jarime , tarikh_khod , tarikh_ghabl):
    # TODO:: have to complete this and i am sleepy and cant do it
    return ekhtelaf_rooz()

def ekhtelaf_rooz(datee1 , datee2):
    sal = {}
    sal[1] = 31
    sal[2] = 31
    sal[3] = 31
    sal[4] = 31
    sal[5] = 31
    sal[6] = 31
    sal[7] = 30
    sal[8] = 30
    sal[9] = 30
    sal[10] = 30
    sal[11] = 30
    sal[12] = 29
    date1 = datee1
    date2 = datee2
    date1 = date1.split('/')
    date2 = date2.split('/')
    if int(date1[0]) - int(date2[0]) == 0:
        roozHa = int(date1[2]) - int(sal[int(date1[1])])
        roozHa = abs(roozHa)
        if int(date1[1]) - int(date2[1]) == 0:
            rooHamoonMah = int(date2[2]) - int(sal[int(date2[1])])
            roozHa = roozHa - abs(rooHamoonMah)
            return roozHa
        roozHa = roozHa + int(date2[2])
        mah = int(date1[1]) - int(date2[1])
        mah = abs(mah)
        # return mah
        mah_shomar = int(date1[2])
        if mah != 0:
            for i in range(mah):
                roozHa = roozHa + int(sal[int(mah_shomar)])
                mah_shomar = mah_shomar + 1
                if mah_shomar == 12:
                    mah_shomar = 1
        return roozHa
    if abs(int(date1[0]) - int(date2[0])) != 0:
        roozHa = int(date1[2]) - int(sal[int(date1[1])])
        roozHa = abs(roozHa)
        roozHa = roozHa + int(date2[2])
        dateee1 = datetime.strptime((datee1) , '%Y/%m/%d')
        dateee2 = datetime.strptime((datee2) , '%Y/%m/%d')
        from dateutil import relativedelta
        diffs = relativedelta.relativedelta(dateee1, dateee2)
        mah = abs(diffs.months)
        print(mah)
        mah = mah +  abs(int(diffs.months))
        print(mah)
        mah = mah + (abs(diffs.years) * 12 )
        mah_shomar = int(date1[2])
        if mah != 0:
            for i in range(mah):
                roozHa = roozHa + int(sal[int(mah_shomar)])
                mah_shomar = mah_shomar + 1
                if mah_shomar == 12:
                    mah_shomar = 1
        return roozHa

app.run(debug=True)
