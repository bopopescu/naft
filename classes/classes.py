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
        # parser.add_argument('tarikh_pardakht_shode')
        parser.add_argument('tarikh_jadid_pardakht')
        parser.add_argument('mohasebe_takhir')
        parser.add_argument('mizan_takhir')
        parser.add_argument('jarime')
        parser.add_argument('mizane_taakhir_dar_mohasebat_ghest')
        parser.add_argument('id_ghest')
        parser.add_argument("file_peyvast",type=werkzeug.datastructures.FileStorage,location = 'files')
        args = parser.parse_args()
        file = args['file_peyvast']
        if file:
            import secrets
            dirname = secrets.dirname
            file.save(os.path.join(dirname, 'files', file.filename))
            fileName = file.filename
            return fileName
        else:
            fileName = None
        sql = "insert into jarime_taakhir_dar_pardakht (shomare_pardakht_be_taakhir_oftade ,mablagh_pardakht, tarikh_barname_pardakht,tarikh_jadid_pardakht,file_peyvast , mohasebe_takhir , mizan_takhir , jarime,mizane_taakhir_dar_mohasebat_ghest,id_ghest) values (%s ,%s , %s ,%s ,%s,%s ,%s ,%s,%s,%s)"
        values = (args['shomare_pardakht_be_taakhir_oftade'],args['mablagh_pardakht'] , args['tarikh_barname_pardakht'] , args['tarikh_jadid_pardakht'] ,  fileName , args['mohasebe_takhir'],args['mizan_takhir'],args['jarime'],args['mizane_taakhir_dar_mohasebat_ghest'],args['id_ghest'])
        mycursor.execute(sql,values)
        mydb.commit()
        return True
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id',required = True)
        args = parser.parse_args()
        mycursor.execute('delete from jarime_taakhir_dar_pardakht where id =%s'+args['id'])
        mydb.commit()
        return True

