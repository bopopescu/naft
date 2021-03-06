from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
from khayyam import *
from datetime import timedelta
from timeFunctions import khayam_type_days


class taakhir_dar_bahre_bardari_tajamoee(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_ghest',required = True)
        args = parser.parse_args()
        i = 1
        pool_tajamoee = 0
        while i <= 1 :
            pools = mohasebe_taakhir(args['id_ghest'] , i)
            pool = pools['jarime']
            for x in pool:
                pool_tajamoee += x[1]
            i +=1
        pool_tajamoee +=pools['jadval_dark2hasti']['taahodat_pardakht_sherkat_naftanir']
        pool_tajamoee +=pools['jadval_dark2hasti']['taahodat_pardakht_sherkat_mohandesi_tose_gas']
        pool_tajamoee +=pools['jadval_dark2hasti']['jarime_taakhir_dar_pardakht']
        return pool_tajamoee




def mohasebe_taakhir(id_ghest , gostare_id):
    # parser = reqparse.RequestParser()
    # parser.add_argument('gostare_id', required=True)
    # parser.add_argument('id_ghest')
    # args = parser.parse_args()
    args = {}
    args['gostare_id'] = gostare_id
    args['id_ghest'] = id_ghest

    mycursor.execute("select * from gostare where id = %s ", (args['gostare_id'],))
    gostare_data = mycursor.fetchall()
    mydb.commit()
    if args['id_ghest']:
        query = "select * from gostare_pishraft where gostare_id = %s and malg =1 and id_ghest =%s"
        values = (args['gostare_id'],args['id_ghest'])
        mycursor.execute(query, values)
    else:
        query = "select * from gostare_pishraft where gostare_id = %s and malg =1"
        values = (args['gostare_id'],)
        mycursor.execute(query, values)
    gostare_pishrafts = mycursor.fetchall()

    jadval_jarime = []
    darsad_tahaghogh_yafte = 0
    for gostare in gostare_pishrafts:
        days_dif = khayam_type_days(gostare[3], gostare_data[0][3])
        jarime = (50000 * int(abs(days_dif)) * float(gostare[2]))
        jadval_jarime.append([gostare[5],jarime,gostare[3],gostare[2],gostare[4]])
        darsad_tahaghogh_yafte += float(gostare[2])
    jadval_koli = {
        'esme_gostare': gostare_data[0][1],
        'vazne_kole_khat': gostare_data[0][2],
        'darsad_tahaghogh_yafte':darsad_tahaghogh_yafte,
        'darsad_baghi_mande': float(gostare_data[0][2]) - darsad_tahaghogh_yafte,
        'tarikh':gostare_data[0][3]
    }
    ret = {}
    ret['jadval_koli'] = jadval_koli
    ret['jarime'] = jadval_jarime
    if args['id_ghest']:
        ret['jadval_dark2hasti'] = shandool(args['id_ghest'])
    else:
        ret['jadval_darkhasti'] = None
    return ret



def shandool(id_ghest):
    # parser = reqparse.RequestParser()
    # parser.add_argument('id_ghest',required=True)
    # args = parser.parse_args()
    query = "select * from taahodat_pardakht_sherkat_naftanir where id_ghest ="+id_ghest
    mycursor.execute(query)
    naftanir = mycursor.fetchall()
    jarimeha = {}
    jarime = 0
    for i in naftanir:
        jarime += float(i[3])
    jarimeha['taahodat_pardakht_sherkat_naftanir'] = jarime
    jarime=0
    query = "select * from taahodat_pardakht_sherkat_mohandesi_tose_gas where id_ghest ="+id_ghest
    mycursor.execute(query)
    tose_gas = mycursor.fetchall()

    for i in tose_gas:
        jarime += float(i[3])
    jarimeha['taahodat_pardakht_sherkat_mohandesi_tose_gas'] = jarime
    jarime = 0
    query = "select * from jarime_taakhir_dar_pardakht where id_ghest ="+id_ghest
    mycursor.execute(query)
    jarime_taakhir_dar_pardakht = mycursor.fetchall()
    mydb.commit()

    for i in jarime_taakhir_dar_pardakht:
        jarime += float(i[2])
    jarimeha['jarime_taakhir_dar_pardakht'] = jarime

    return jarimeha
