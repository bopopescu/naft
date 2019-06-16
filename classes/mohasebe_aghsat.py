from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
import pandas
import json

class mohasebe_aghsat(Resource):
    def get(self):
        model_mali_csv = pandas.read_csv('gharar_dad.csv')
        df = pandas.DataFrame(model_mali_csv)
        i = 0
        res = []
        while i < 43:
            s = df.iloc[[i]].values.tolist()
            # s = tuple(s[0])
            # print(s)
            res.insert(i,s[0])
            i += 1
        return res