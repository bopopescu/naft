from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
from khayyam import *
from datetime import timedelta
from timeFunctions import khayam_type_days


class jaraem_taakhir_dar_bahre_bardariV2(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gostare_id', required=True)
        args = parser.parse_args()

        mycursor.execute("select * from gostare where id = %s ", (args['gostare_id'],))
        gostare_data = mycursor.fetchall()
        mydb.commit()
        query = "select * from gostare_pishraft where gostare_id = %s and malg =1"
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
        jadval_koli = {
            'esme_gostare': gostare_data[0][1],
            'vazne_kole_khat': gostare_data[0][2],
            'darsad_tahaghogh_yafte':darsad_tahaghogh_yafte,
            'darsad_baghi_mande': float(gostare_data[0][2]) - darsad_tahaghogh_yafte
        }
        ret = {}
        ret['jadval_koli'] = jadval_koli
        ret['jarime'] = jadval_jarime
        return ret
