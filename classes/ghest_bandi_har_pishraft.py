from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
import pandas
import json


class ghest_bandi_har_pishraft(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gostare_id',required=True)
        args = parser.parse_args()

        query = "select * from gostare_pishraft where gostare_id = %s"
        values = (args['gostare_id'] ,)
        mycursor.execute(query , values)
        gostare_pishrafts = mycursor.fetchall()

        ret = {}
        for gostare_pishraft in gostare_pishrafts:
            i = 0
            ret[str(gostare_pishraft[5])] = []
            while i < 29:
                id = i
                i += 1
        # for gostare_pishraft in gostare_pishrafts:
        #     return gostare_pishraft
        df = self.opencsv()
        print (df.loc[0:29,"15.10%"])
        return "s"
    def opencsv(self):
        model_mali_csv = pandas.read_csv('model_mali.csv')
        print (type(model_mali_csv))
        df = pandas.DataFrame(model_mali_csv)
        return df