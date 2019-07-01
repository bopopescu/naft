from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
from khayyam import *
from datetime import timedelta
from timeFunctions import khayam_type_days


class jaraem_taakhir_dar_bahre_bardari_tajamoe(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('ghest_id', required=True)
        args = parser.parse_args()

        # mycursor.execute("select * from gostare where id = %s ", (args['gostare_id'],))
        # gostare_data = mycursor.fetchall()
        # mydb.commit()
        # query = "select * from gostare_pishraft where gostare_id = %s"
        # values = (args['gostare_id'],)
        # mycursor.execute(query, values)
        # gostare_pishrafts = mycursor.fetchall()
        #
        # jadval_jarime = []
        # darsad_tahaghogh_yafte = 0
        # for gostare in gostare_pishrafts:
        #     days_dif = khayam_type_days(gostare[3], gostare_data[0][3])
        #     jarime = (50000 * int(abs(days_dif)) * float(gostare[2]))
        #     jadval_jarime.append([gostare[5],jarime,gostare[3],gostare[2]])
        #     darsad_tahaghogh_yafte += float(gostare[2])
        # jadval_koli = {
        #     'esme_gostare': gostare_data[0][1],
        #     'vazne_kole_khat': gostare_data[0][2],
        #     'darsad_tahaghogh_yafte':darsad_tahaghogh_yafte,
        #     'darsad_baghi_mande': float(gostare_data[0][2]) - darsad_tahaghogh_yafte
        # }
        # ret = {}
        # ret['jadval_koli'] = jadval_koli
        # ret['jarime'] = jadval_jarime
        # return ret
        ghests = ()
        ghest_number = int(args['ghest_id'])
        while ghest_number >= 1:
            ghests = ghests + (ghest_number,)
            ghest_number = ghest_number - 1
        # print (type(ghests))
        # print(type(ghest_number))
        print(type(args['ghest_id']))
        if int(args['ghest_id']) == 1 :
            # return "salam"
            # sql = "select * from gostare_pishraft where id_ghest = " + str(1)
            # print(sql)
            mycursor.execute("select * from gostare_pishraft where id_ghest = " + str(1))
            pishrafts = mycursor.fetchall()
        else:
            mycursor.execute("select * from gostare_pishraft where id_ghest in "+ str(ghests))
            pishrafts = mycursor.fetchall()
        id_gostare_ha =  ()
        for gostare in pishrafts:
            # days_dif = khayam_type_days(gostare[3], gostare_data[0][3])
            # jarime = (50000 * int(abs(days_dif)) * float(gostare[2]))
            if (int(gostare[1]) in id_gostare_ha):
                print ("yes")
            else:
                id_gostare_ha = id_gostare_ha + (int(gostare[1]),)
        mycursor.execute('select * from gostare where id  in'+ str(id_gostare_ha))
        gostareHa = mycursor.fetchall()
        mablaghe_koli = 0
        for gostare in gostareHa:
            mablaghe_koli = mablaghe_koli  + self.get2(gostare[0])[0][1]
        return mablaghe_koli


    def get2(self , gostare_id):
        args = {}
        args['gostare_id'] = gostare_id
        mycursor.execute("select * from gostare where id = %s ", (args['gostare_id'],))
        gostare_data = mycursor.fetchall()
        mydb.commit()
        query = "select * from gostare_pishraft where gostare_id = %s"
        values = (args['gostare_id'],)
        mycursor.execute(query, values)
        gostare_pishrafts = mycursor.fetchall()

        jadval_jarime = []
        darsad_tahaghogh_yafte = 0
        for gostare in gostare_pishrafts:
            days_dif = khayam_type_days(gostare[3], gostare_data[0][3])
            jarime = (50000 * int(abs(days_dif)) * float(gostare[2]))
            jadval_jarime.append([gostare[5],jarime,gostare[3],gostare[2]])
            darsad_tahaghogh_yafte += float(gostare[2])
        # jadval_koli = {
        #     'esme_gostare': gostare_data[0][1],
        #     'vazne_kole_khat': gostare_data[0][2],
        #     'darsad_tahaghogh_yafte':darsad_tahaghogh_yafte,
        #     'darsad_baghi_mande': float(gostare_data[0][2]) - darsad_tahaghogh_yafte
        # }
        ret = {}
        # ret['jadval_koli'] = jadval_koli
        ret['jarime'] = jadval_jarime
        return ret['jarime']