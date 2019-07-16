from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
import pandas
import json

class mohasebe_aghsat_tajamoee(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id_ghest',required=True)
        args = parser.parse_args()

        query = "select * from taahodat_pardakht_sherkat_naftanir where id_ghest ="+args['id_ghest']
        mycursor.execute(query)
        naftanir = mycursor.fetchall()
        jarimeha = {}
        jarime = 0
        for i in naftanir:
            jarime += float(i[3])
        jarimeha['taahodat_pardakht_sherkat_naftanir'] = jarime
        jarime=0
        query = "select * from taahodat_pardakht_sherkat_mohandesi_tose_gas where id_ghest ="+args['id_ghest']
        mycursor.execute(query)
        tose_gas = mycursor.fetchall()

        for i in tose_gas:
            jarime += float(i[3])
        jarimeha['taahodat_pardakht_sherkat_mohandesi_tose_gas'] = jarime
        jarime = 0
        query = "select * from jarime_taakhir_dar_pardakht where id_ghest ="+args['id_ghest']
        mycursor.execute(query)
        jarime_taakhir_dar_pardakht = mycursor.fetchall()
        mydb.commit()

        for i in jarime_taakhir_dar_pardakht:
            jarime += float(i[2])
        jarimeha['jarime_taakhir_dar_pardakht'] = jarime

        return jarimeha
