from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
api = Api(app)
import DB as db
import mysql.connector


class gostare(Resource):

    def get(self):
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
        if args['mahe_khali'] and args['id_gostare']:
            values =  ( int(args['id_gostare']) ,0 ,args['mahe_khali'] ,)
            # print(values)
            db.mycursor.execute("INSERT INTO gostare_pishraft(gostare_id , darsad , tarikh) values (%s , %s , %s)", values)
            db.mydb.commit()

        if args['darsade_bardari'] and args['tarikh'] and args['id_gostare']:
            values = (args['id_gostare'],args['darsade_bardari'] , args['tarikh'] , )
            # print(values)
            db.mycursor.execute("INSERT INTO gostare_pishraft(gostare_id , darsad , tarikh) values (%s , %s , %s)", values)
            db.mydb.commit()
        return args["mahe_khali"]

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
        args = parser.parse_args()
        db.mycursor.execute("INSERT INTO peymankaran (check_id , check_money , tarikh , tozihat) VALUES (%s , %s ,%s , %s)" , (args['check_id'],args['money'],args['tarikh'] , args['tozih'] , ))
        db.mydb.commit()
        return "saved"
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
        parser = reqparse.RequestParser()
        parser.add_argument("type")
        parser.add_argument("date")
        parser.add_argument("money")
        args = parser.parse_args()
        sql = "INSERT INTO arazi (type , date , money) VALUES (%s , %s , %s)"
        values = (args['type'] , args['date'] , args['money'] ,)
        db.mycursor.execute(sql , values)
        db.mydb.commit()
        return "saved"
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
        parser.add_argument('hazineSodoor')
        parser.add_argument('hazineBime')
        args = parser.parse_args()
        
        # mysql = "INSERT INTO pipelinesf (tarikh ,zekhamat , metraj , tonaj , tarikhTahvil,typeKalaTahvil ,shomareHavaleAnbar , shomareTaghaza,shomareGhalam ,nerkhTashilBankMarkazi ,hazineAnbar , hazineSodoor, hazineBime , mablagheVaragh , avarezGomrok , hazineSakhteLoole , hazinePooshesh , maliatVaragh, maliatSakht )"
        mysql = "INSERT INTO pipelinesf (" \
                "tarikh ," \
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
                "hazineSodoor, " \
                "hazineBime ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (args['tarikh'] ,
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
                  args['hazineSodoor'],
                  args['hazineBime'],)
        db.mycursor.execute(mysql ,values)
        db.mydb.commit()
        return "saved"
    
    def get(self):
        db.mycursor.execute("SELECT * FROM pipelinesf")
        ret = db.mycursor.fetchall()
        return ret


api.add_resource(gostare,"/gostare")
api.add_resource(peymankaran,"/peymankaran")
api.add_resource(pipeLinesF,"/pipeLinesF")
api.add_resource(arazi , "/arazi")


app.run(debug=True)
