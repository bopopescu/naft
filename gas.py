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
            #values =  ( float(args['id_gostare']) ,0 ,args['mahe_khali'] ,)
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
        parser.add_argument('Inch36')
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
                  args['Inch36'],args['tarikh'])
        db.mycursor.execute(mysql ,values)
        db.mydb.commit()
        return True
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("inch36")
        args = parser.parse_args()
        if args['inch36']:
            db.mycursor.execute("SELECT * FROM pipelinesf WHERE se IS NOT NULL ")
        else:
            db.mycursor.execute("SELECT * FROM pipelinesf WHERE se IS NULL")
        data = db.mycursor.fetchall()
        ret = {}
        i = 0
        for record in data:
            mablaghe_varagh = float(record[3])*1033
            avarez_gomrok = mablaghe_varagh * float(record[9]) * 4/100
            # maliyat_bar_arzesh_afzoode_varagh = avarez_gomrok * 1/10
            hazine_sakht_loole = 0
            if record[5] == "ورق" :
                hazine_sakht_loole = 0
                hazine_pooshesh = 0
            else :
                hazine_sakht_loole = float(record[3]) * 125
                hazine_pooshesh = 0
            if record[5] == "پوشش داده شده":
                hazine_sakht_loole = float(record[3])*95
                hazine_pooshesh = float(record[3]) * 125
            maliyat_bar_arzesh_afzoode_sakht_pooshesh = (hazine_sakht_loole + hazine_pooshesh) *  float(record[9]) * 10/100
            maliyat_bar_arzesh_afzoode_varagh = ((mablaghe_varagh * float(record[9])) + float(record[10]) + float(record[11]) + avarez_gomrok) * 1 / 10
            motalebate_riyali = float(record[10]) + float(record[11]) + avarez_gomrok + maliyat_bar_arzesh_afzoode_varagh + maliyat_bar_arzesh_afzoode_sakht_pooshesh
            motalebat_arzi = hazine_pooshesh + hazine_sakht_loole

            ret[i] ={'dataBase' : record ,
                             'mablaghe_varagh':mablaghe_varagh,
                             'avarez_gomrok':avarez_gomrok,
                             'maliyat_bar_arzesh_varagh':maliyat_bar_arzesh_afzoode_varagh,
                             'hazine_sakhte_loole':hazine_sakht_loole,
                             'hazine_pooshesh':hazine_pooshesh,
                             'maliyat_bara_arzesh_afzoode_sakhte_pooshesh':maliyat_bar_arzesh_afzoode_sakht_pooshesh,
                             'motalebat_riyali':motalebate_riyali,
                             'motalebat_arzi':motalebat_arzi}
            i = i+ 1
        return ret

    def get2(self):
        parser = reqparse.RequestParser()
        parser.add_argument("inch36")
        args = parser.parse_args()
        # if args['inch36']:
        db.mycursor.execute("SELECT * FROM pipelinesf")
        data = db.mycursor.fetchall()
        ret = {}
        i = 0
        for record in data:
            mablaghe_varagh = float(record[3])*1033
            avarez_gomrok = mablaghe_varagh * float(record[9]) * 4/100
            # maliyat_bar_arzesh_afzoode_varagh = avarez_gomrok * 1/10
            hazine_sakht_loole = 0
            if record[5] == "ورق" :
                hazine_sakht_loole = 0
                hazine_pooshesh = 0
            else :
                hazine_sakht_loole = float(record[3]) * 125
                hazine_pooshesh = 0
            if record[5] == "پوشش داده شده":
                hazine_sakht_loole = float(record[3])*95
                hazine_pooshesh = float(record[3]) * 125
            maliyat_bar_arzesh_afzoode_sakht_pooshesh = (hazine_sakht_loole + hazine_pooshesh) *  float(record[9]) * 10/100
            maliyat_bar_arzesh_afzoode_varagh = ((mablaghe_varagh * float(record[9])) + float(record[10]) + float(record[11]) + avarez_gomrok) * 1 / 10
            motalebate_riyali = float(record[10]) + float(record[11]) + avarez_gomrok + maliyat_bar_arzesh_afzoode_varagh + maliyat_bar_arzesh_afzoode_sakht_pooshesh
            motalebat_arzi = hazine_pooshesh + hazine_sakht_loole

            ret[i] ={'dataBase' : record ,
                             'mablaghe_varagh':mablaghe_varagh,
                             'avarez_gomrok':avarez_gomrok,
                             'maliyat_bar_arzesh_varagh':maliyat_bar_arzesh_afzoode_varagh,
                             'hazine_sakhte_loole':hazine_sakht_loole,
                             'hazine_pooshesh':hazine_pooshesh,
                             'maliyat_bara_arzesh_afzoode_sakhte_pooshesh':maliyat_bar_arzesh_afzoode_sakht_pooshesh,
                             'motalebat_riyali':motalebate_riyali,
                             'motalebat_arzi':motalebat_arzi}
            i = i+ 1
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
                              'natayej_motalebat': (float(record[4]) * (float(record[5])/float(record[6])))}
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
        parser.add_argument("state")
        args = parser.parse_args()
        db.mycursor.execute("INSERT INTO pardakht_shode_tavasote_naftanir_tm (tarikh , mablagh , pardakht_shod_babate,shomare_sanad, tozihat , state) VALUES (%s,%s,%s,%s,%s)",
                            (args['tarikh'] , args['mablagh'],args['pardakht_shod_babate'],args['shomare_sanad'],args['tozihat'],args['state']))
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
        # ret['miyangin']=(float(data[0][1])+float(data[0][2])+float(data[0][3])) / 3
        # ret['shandool']= "shandool"
        miyangin = {}
        # return data
        for record in data:
            ret['database_record'+str(record[0])] = float(record[1]),float(record[2]),float(record[3])
            ret['miyangin__'+str(record[0])] = (float(record[1]) + float(record[2]) + float(record[3])) / 3
            ret['maliayt__'+str(record[0])] = ((float(record[1]) + float(record[2]) + float(record[3])) / 3) * 1/10
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
        parse = reqparse.RequestParser()
        parse.add_argument("money")
        parse.add_argument("asl_dar_mohasebat")
        parse.add_argument("tarikh")
        parse.add_argument("jarime")
        args = parse.parse_args()
        db.mycursor.execute("INSERT INTO sadid_mahshahr(money , asl_dar_mohasebat , tarikh , jarime)  VALUES(%s , %s ,%s , %s) " , (args['money'] , args['asl_dar_mohasebat'],args['tarikh'],args['jarime'],))
        db.mydb.commit()
        return True
from operator import itemgetter
import operator
class jadval56(Resource):
    def get(self):
        # p56 = pipeLinesF()
        # p56 =  p56.get2()
        # p56 = json.dumps(p56)
        # p56 = json.loads(p56)
        # # pipeline56 = {}
        # for id in  p56:
        #      pipeline56[id] = {}
        #      pipeline56[id]['taahod_be_pardakht'] = p56[id]['motalebat_riyali']
        #      # jareme = jarime(1 ,1 ,1 ,1)
        #      pipeline56[id]['jarime'] = 1
        #      if float(id) == 1:
        #         pndg = 0
        #      else:
        #         pndg = pipeline56[str(float(id) - 1)]['kole_motalebat']
        #      pipeline56[id]['pardakht_nashode_dore_ghable'] = pndg
        #      pipeline56[id]['kole_motalebat'] = float(pipeline56[id]['jarime']) + pndg + pipeline56[id]['taahod_be_pardakht']
        # return pipeline56
        db.mycursor.execute("select * from pardakht_shode_tavasote_naftanir_tm where pardakht_shod_babate = %s" ,("لوله",))
        naftanir = db.mycursor.fetchall()
        db.mycursor.execute("SELECT * FROM pipelinesf")
        p56 = db.mycursor.fetchall()
        merger ={}
        i = 0
        for record in p56:

            mablaghe_varagh = float(record[3]) * 1033
            avarez_gomrok = mablaghe_varagh * float(record[9]) * 4 / 100
            hazine_sakht_loole = 0
            if record[5] == "ورق":
                hazine_sakht_loole = 0
                hazine_pooshesh = 0
            else:
                hazine_sakht_loole = float(record[3]) * 125
                hazine_pooshesh = 0
            if record[5] == "پوشش داده شده":
                hazine_sakht_loole = float(record[3]) * 95
                hazine_pooshesh = float(record[3]) * 125
            maliyat_bar_arzesh_afzoode_sakht_pooshesh = (hazine_sakht_loole + hazine_pooshesh) * float(
                record[9]) * 10 / 100
            maliyat_bar_arzesh_afzoode_varagh = ((mablaghe_varagh * float(record[9])) + float(record[10]) + float(
                record[11]) + avarez_gomrok) * 1 / 10
            motalebate_riyali = float(record[10]) + float(record[
                                                              11]) + avarez_gomrok + maliyat_bar_arzesh_afzoode_varagh + maliyat_bar_arzesh_afzoode_sakht_pooshesh
            motalebat_arzi = hazine_pooshesh + hazine_sakht_loole

            ret = {'dataBase': record,
                      'mablaghe_varagh': mablaghe_varagh,
                      'avarez_gomrok': avarez_gomrok,
                      'maliyat_bar_arzesh_varagh': maliyat_bar_arzesh_afzoode_varagh,
                      'hazine_sakhte_loole': hazine_sakht_loole,
                      'hazine_pooshesh': hazine_pooshesh,
                      'maliyat_bara_arzesh_afzoode_sakhte_pooshesh': maliyat_bar_arzesh_afzoode_sakht_pooshesh,
                      'motalebat_riyali': motalebate_riyali,
                      'motalebat_arzi': motalebat_arzi}

            d1 = moment.date(record[13]).strftime("%Y-%m-%d")
            d2 = moment.date("1350-1-1").strftime("%Y-%m-%d")
            d1 = moment.date(d1).locale("Asia/Tehran").date
            d2 = moment.date(d2).locale("Asia/Tehran").date
            ekh = d1 - d2
            ekh = str(ekh)
            ekh = ekh.split(' ')
            merger[i] = {
                'pool':ret['motalebat_riyali'],
                'tarikh': record[13],
                'ekhtelaf': int(ekh[0]),
                'sharh':"loole"
            }
            i = i+1
        for n in naftanir:
            d1 = moment.date(n[1]).strftime("%Y-%m-%d")
            d2 = moment.date("1350-1-1").strftime("%Y-%m-%d")
            d1 = moment.date(d1).locale("Asia/Tehran").date
            d2 = moment.date(d2).locale("Asia/Tehran").date
            ekh = d1 - d2
            ekh = str(ekh)
            ekh = ekh.split(' ')
            merger[i] = {
                'pool':n[2],
                'tarikh':n[1],
                'ekhtelaf': int(ekh[0]),
                'sharh':'naftanir'
            }
            i = i +1
        db.mycursor.execute("select * from jadval56")
        jadvals = db.mycursor.fetchall()
        for i in jadvals:
            db.mycursor.execute('delete from jadval56 where id =%s',(i[0],))
        db.mydb.commit()
        for i in merger:
            db.mycursor.execute("insert into jadval56 (pool , tarikh , ekhtelaf,sharh ) VALUES (%s , %s ,%s ,%s)" , (merger[i]['pool'],
                                                                                                                     merger[i]['tarikh'],
                                                                                                                     merger[i]['ekhtelaf'],
                                                                                                                     merger[i]['sharh']))
            db.mydb.commit()

        db.mycursor.execute("select * from jadval56")
        data = db.mycursor.fetchall()
        jadval = {}
        nerkh_jarime = 1
        i = 0
        for n in data:
            if i == 0:
                jarime_dore_ghabl =0
                pardakht_nashode_dore_ghabl = 0
                kole_motalebat = 0
            else:
                pardakht_nashode_dore_ghabl = jadval[i-1]['jame_kole_motalebat']
                jarime_dore_ghabl = (pardakht_nashode_dore_ghabl * ( 1 + nerkh_jarime)**(ekhtelaf_date(jadval[i-1]['tarikh'],data[i][2]))) - pardakht_nashode_dore_ghabl
            if data[i][4] == 'naftanir':
                sharh = "پرداخت شده توسط نفتانیر"
                tarikh = data[i][2]
                pool = float(data[i][1]) * -1
            else:
                pool = abs(float(data[i][1]))
                sharh = data[i][4]
            jadval[i] = {
                'sharh':sharh,
                'tarikh':data[i][2],
                'pool':pool,
                'jarime':jarime_dore_ghabl,
                'jame_kole_motalebat': jarime_dore_ghabl + jarime_dore_ghabl + pool
            }
            i = i+1
        return jadval


class jadvalArazi(Resource):
    def get(self):
        arz = arazi()
        arz = arz.get()
        arz = json.dumps(arz)
        arz = json.loads(arz)
        jarazi = {}
        jarazi['0'] = {
            'sharh' : "مبلغ ریالی پرداخت شده",
            'tarikh' : '1394-12-27',
            'pardakht_shode_tavasote_naftanir': 85747896194,
            'taahod_be_pardakht': 0,
            'pardakht_nashode_dore_ghabl': 0,
            'jarime' : 0,
            'motalebat':-85747896194,
        }
        nerkh_jarime = 1
        i = 1
        for id in arz:
            jarazi[i] ={}
            jarazi[i]['sharh'] = 'مبالغ ریالی در تعهد'
            jarazi[i]['tarikh'] = '1394-12-27'
            jarazi[i]['pardakht_shode_tavasote_naftanir'] = 0
            jarazi[i]['taahod_be_pardakht'] = arz[i-1][3]
            jarazi[i]['tarikh_taaid_hoghooghi'] = arz[i-1][4]
            taahod = arz[i-1][3]
            # taahod = arz[i-1][3]
            jarazi[i]['kole_motalebat'] = int(taahod) - 85747896194
            # jarazi[i]['kole_motalebat'] = 0
            jarazi[i]['jarime'] = 0
            i = i+1
        return jarazi

class looleSaziSadid(Resource):
    def get(self):
        db.mycursor.execute('select * from sadid_mahshahr')
        data = db.mycursor.fetchall()
        if not data:
            return None
        i = 0
        ret = {}
        nerkh = 0.0180885824835107
        while i <= 2:
            print(i)
            ret[i] = {}
            ret[i]['taahod_be_pardakht'] = float(data[0][1])/3

            if i ==0:
                ret[i]['pardakht_nashod_dore_ghabl'] = 0
                ret[i]['jarime'] = 0
                ret[i]['kole_motalebat'] = float(data[0][1])/3
            if i == 1:
                ret[i]['pardakht_nashod_dore_ghabl'] = ret[i-1]['taahod_be_pardakht']
                ret[i]['jarime'] = (ret[i-1]['kole_motalebat'] *(1+nerkh)**(
                    khayam_type('1394-12-27','1395-01-27'))) -ret[i-1]['kole_motalebat']
                ret[i]['kole_motalebat'] = ret[i]['jarime'] + ret[i-1]['kole_motalebat']+(float(data[0][1])/3)
            if i ==2:
                ret[i]['pardakht_nashod_dore_ghabl'] = ret[i-1]['taahod_be_pardakht']
                ret[i]['jarime'] = (ret[i-1]['kole_motalebat'] *(1+nerkh)**(
                    khayam_type('1395-01-27','1395-02-27'))) -ret[i-1]['kole_motalebat']
                ret[i]['kole_motalebat'] = ret[i]['jarime'] + ret[i - 1]['kole_motalebat'] + (float(data[0][1]) / 3)
            i = i+1
        parser = reqparse.RequestParser()
        parser.add_argument('time_now')
        args = parser.parse_args()
        if args['time_now']:
            ret['end'] = {}
            ret['end']['jarime'] = (ret[2]['kole_motalebat'] * (1+nerkh)**khayam_type('1395-02-27' , args['time_now'])) -  ret[2]['kole_motalebat']
            ret['end']['kole_motalebat'] = ret[2]['kole_motalebat'] + ret['end']['jarime']
        return  ret


import moment
from datetime import datetime
def ekhtelaf_date(date1 , date2):
    d1 =moment.date(date1).strftime("%Y-%m-%d")
    d1 = moment.date(d1).locale("Asia/Tehran").date
    print(d1)
    d2 =moment.date(date2).strftime("%Y-%m-%d")
    d2 = moment.date(d2).locale("Asia/Tehran").date
    print(d2)
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
    sal[11] = 30
    sal[12] = 29
    ekh = d1 - d2
    print(ekh)
    ekh = ekh.days
    date2 = date2.split('-')
    return float(int(ekh) / int(sal[int(date2[1])]))


def ekhtelaf_dateV2(date1 , date2):
    d1 =moment.date(date1).strftime("%Y-%m-%d")
    d1 = moment.date(d1).locale("Asia/Tehran").date
    # print(d1)
    d2 =moment.date(date2).strftime("%Y-%m-%d")
    d2 = moment.date(d2).locale("Asia/Tehran").date
    # print(d2)
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
    sal[11] = 30
    sal[12] = 29
    rooz_aval = str(d1).split('-')
    mah_aval = rooz_aval[1]
    rooz_aval = int(str(rooz_aval[2]).split(' ')[0]) - sal[int(mah_aval)]
    # print(rooz_aval)
    rooz_dovom = str(d2).split('-')
    rooz_dovom = str(rooz_dovom[2]).split(' ')[0]
    # print (rooz_dovom)
    # print('finally')
    ekhtelaf_roozha = int(rooz_dovom) - int(rooz_aval-1)
    # print (ekhtelaf_roozha)
    # print( float(ekhtelaf_roozha / int(sal[int(date2[1])])))
    return float(ekhtelaf_roozha / int(sal[int(date2[1])]))
from khayyam import *
def khayam_type(date1 , date2):
    d1 = date1.split('-')
    d2 = date2.split('-')
    time = JalaliDate(d1[0],d1[1],d1[2])
    time2 = JalaliDate(d2[0],d2[1],d2[2])
    time = time - time2
    days = abs(int(time.days))
    return days/int(time2.daysinmonth)
class jadvalPeymankaran(Resource):
    def get(self):
        nerkh = 0.0180885824835107
        db.mycursor.execute("SELECT * FROM peymankaran")
        jadval = db.mycursor.fetchall()

        sql = "SELECT * FROM pardakht_shode_tavasote_naftanir_tm where pardakht_shod_babate =  پیمانکاران AND state = before"
        # sql = "SELECT * FROM pardakht_shode_tavasote_naftanir_tm"
        db.mycursor.execute(sql)
        jadval_naftanir = db.mycursor.fetchall()
        return jadval_naftanir
        i = 0
        while i< len(jadval_naftanir):
            apending = [
                jadval_naftanir[i][0],
                'پرداخت شده توسط نفتانیر',
                'no_check_id',
                jadval_naftanir[i][2],
                jadval_naftanir[i][1],
                jadval_naftanir[i][5]
                ]
            i = i+1
            jadval.append(apending)
        ret = {}
        i = 0
        while i < len(jadval):
            ret[i]={}
            ret[i]['sharh'] = 'مبلغ ریالی پرداخت شده'
            ret[i]['noe'] = jadval[i][1]
            ret[i]['tozihat'] = jadval[i][5]
            ret[i]['tarikh'] = jadval[i][4]
            ret[i]['pool']=jadval[i][3]
            if i == 0:
                db.mycursor.execute("select * from naftanir_peymankaran_adam")
                dore_ghable_db = db.mycursor.fetchall()
                n = 0
                dore_ghable = 0
                while n < len(dore_ghable_db):
                    dore_ghable = float(dore_ghable_db[n][2]) + float(dore_ghable)
                    n = n+1
                ret[i]['pardakht_nashode_dore_ghable'] = abs(dore_ghable )* -1
                ret[i]['jarime'] = 0
            else:
                ret[i]['pardakht_nashode_dore_ghable'] = ret[i-1]['kole_motalebat']
                ret[i]['jarime'] = (float(ret[i]['pardakht_nashode_dore_ghable']) * (1 + nerkh) ** (
                    abs(khayam_type(jadval[i-1][4], jadval[i][4])))) - float(
                    ret[i]['pardakht_nashode_dore_ghable'])
            ret[i]['kole_motalebat'] = float(ret[i]['jarime']) + float(ret[i]['pardakht_nashode_dore_ghable']) + float(ret[i]['pool'])
            i = i+1
        return ret



class adam_ghateyat_peymankaran(Resource):
    def get(self):
        db.mycursor.execute('select * from naftanir_peymankaran_adam')
        data = db.mycursor.fetchall()
        return data
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('tarikh')
        parser.add_argument('mablagh')
        parser.add_argument('pardakht_shod_babate')
        parser.add_argument('shomare_sanad')
        parser.add_argument('tozihat')
        args = parser.parse_args()
        db.mycursor.execute('insert into naftanir_peymankaran_adam (tarikh,mablagh,pardakht_shod_babate,shomare_sanad,tozihat)'
                            'values(%s,%s,%s,%s,%s)',(args['tarikh'],args['mablagh'],args['pardakht_shod_babate'],args['shomare_sanad'],args['tozihat']))
        db.mydb.commit()
        return True






api.add_resource(adam_ghateyat_peymankaran,"/naftanir_aadam_ghatiyat_peymankaran")
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
    if float(date1[0]) - float(date2[0]) == 0:
        roozHa = float(date1[2]) - float(sal[float(date1[1])])
        roozHa = abs(roozHa)
        if float(date1[1]) - float(date2[1]) == 0:
            rooHamoonMah = float(date2[2]) - float(sal[float(date2[1])])
            roozHa = roozHa - abs(rooHamoonMah)
            return roozHa
        roozHa = roozHa + float(date2[2])
        mah = float(date1[1]) - float(date2[1])
        mah = abs(mah)
        # return mah
        mah_shomar = float(date1[2])
        if mah != 0:
            for i in range(mah):
                roozHa = roozHa + float(sal[float(mah_shomar)])
                mah_shomar = mah_shomar + 1
                if mah_shomar == 12:
                    mah_shomar = 1
        return roozHa
    if abs(float(date1[0]) - float(date2[0])) != 0:
        roozHa = float(date1[2]) - float(sal[float(date1[1])])
        roozHa = abs(roozHa)
        roozHa = roozHa + float(date2[2])
        dateee1 = datetime.strptime((datee1) , '%Y/%m/%d')
        dateee2 = datetime.strptime((datee2) , '%Y/%m/%d')
        from dateutil import relativedelta
        diffs = relativedelta.relativedelta(dateee1, dateee2)
        mah = abs(diffs.months)
        print(mah)
        mah = mah +  abs(float(diffs.months))
        print(mah)
        mah = mah + (abs(diffs.years) * 12 )
        mah_shomar = float(date1[2])
        if mah != 0:
            for i in range(mah):
                roozHa = roozHa + float(sal[float(mah_shomar)])
                mah_shomar = mah_shomar + 1
                if mah_shomar == 12:
                    mah_shomar = 1
        return roozHa

app.run(debug=True)
