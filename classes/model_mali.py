from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
import pandas
import json

class model_mali(Resource):
    def get(self):
        model_mali_csv = pandas.read_csv('model_mali.csv')
        df = pandas.DataFrame(model_mali_csv)
        # df = df.to_json()
        # resp = make_response(df.to_json(orient="records"))
        # return json.dumps(df)
        i = 0
        res = []
        while i < 30:
            s = df.iloc[[i]].values.tolist()
            # s = tuple(s[0])
            # print(s)
            res.insert(i,s[0])
            i += 1
        return res