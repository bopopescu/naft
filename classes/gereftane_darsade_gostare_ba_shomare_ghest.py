from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
import pandas
import json


class gereftane_darsade_gostare_ba_shomare_ghest(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('shomare_ghest',required=True)
        args = parser.parse_args()

        query = "select * from gostare_pishraft where id_ghest = %s"
        values = (args['shomare_ghest'] ,)
        mycursor.execute(query , values)
        res = mycursor.fetchall()
        return res
