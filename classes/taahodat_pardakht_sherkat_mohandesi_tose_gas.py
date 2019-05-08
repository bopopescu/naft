from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse

class taahodat_pardakht_sherkat_mohandesi_tose_gas(Resource):
    def get(self):
        mycursor.execute("select * from taahodat_pardakht_sherkat_mohandesi_tose_gas")
        data = mycursor.fetchall()
        return data
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('tarikh')
        parser.add_argument('sharh')
        parser.add_argument('mablagh_dollar')
        parser.add_argument('tozihat')
        parser.add_argument("file_peyvast", type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        file = args['file_peyvast']
        if file:
            dirname = os.path.dirname(__file__)
            file.save(os.path.join(dirname, 'files', file.filename))
            fileName = file.filename
        else:
            fileName = None
        sql = "INSERT INTO taahodat_pardakht_sherkat_mohandesi_tose_gas (tarikh , sharh,mablagh_dollari,tozihat,file_peyvast) VALUES (%s,%s,%s,%s,%s)"
        values = (args['tarikh'] , args['sharh'] , args['mablagh_dollar'] , args['tozihat'] , fileName)
        mycursor.execute(sql,values)
        mydb.commit()
        return True