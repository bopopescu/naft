from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse

class jarime_takhir_dar_pardakht(Resource):
    def get(self):
        mycursor.execute('select * from jarime_taakhir_dar_pardakht')
        datas = mycursor.fetchall()
        return datas

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('shomare_pardakht_be_taakhir_oftade')
        parser.add_argument('mablagh_pardakht')
        parser.add_argument('tarikh_barname_pardakht')
        parser.add_argument('tarikh_jadid_pardakht')
        parser.add_argument('mizane_taakhir_dar_mohasebat_ghest')
        parser.add_argument("file_peyvast",type=werkzeug.datastructures.FileStorage,location = 'files')
        args = parser.parse_args()
        file = args['file_peyvast']
        if file:
            dirname = os.path.dirname(__file__)
            file.save(os.path.join(dirname, 'files', file.filename))
            fileName = file.filename
        else:
            fileName = None
        sql = "insert into jarime_taakhir_dar_pardakht (shomare_pardakht_be_taakhir_oftade ,mablagh_pardakht, tarikh_barname_pardakht,tarikh_jadid_pardakht,mizane_taakhir_dar_mohasebat_ghest,file_peyvast) values (%s ,%s , %s ,%s ,%s,%s)"
        values = (args['shomare_pardakht_be_taakhir_oftade'],args['mablagh_pardakht'] , args['tarikh_barname_pardakht'] , args['tarikh_jadid_pardakht'] , args['mizane_taakhir_dar_mohasebat_ghest'] , fileName)
        mycursor.execute(sql,values)
        mydb.commit()
        return True
