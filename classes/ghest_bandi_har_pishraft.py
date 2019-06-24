from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
import pandas
import json
from timeFunctions import *
from dateutil.relativedelta import *
from datetime import timedelta
from khayyam import JalaliDate


class ghest_bandi_har_pishraft(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gostare_id',required=True)
        args = parser.parse_args()



        mycursor.execute("select * from gostare where id = %s ",(args['gostare_id'],))
        gostare_data = mycursor.fetchall()
        mydb.commit()
        query = "select * from gostare_pishraft where gostare_id = %s"
        values = (args['gostare_id'] ,)
        mycursor.execute(query , values)
        gostare_pishrafts = mycursor.fetchall()

        df = self.opencsv()
        column = df.loc[0:29 , str(gostare_data[0][2]) + "%"]
        ret = {}
        i = 0
        for gostare_pishraft in gostare_pishrafts:
            ret[gostare_pishraft[5]] = {}

            d = gostare_pishraft[3].split('-')
            time = JalaliDate(d[0], d[1], d[2])
            month = int(d[1])
            while i < 29:
                if month > 12 :
                    month = 1
                    d[0] = str(int(d[0])+1)
                column[i]= column[i].replace(',', '')
                ret[gostare_pishraft[5]][i] = [
                    float(gostare_pishraft[2])/float(gostare_data[0][2]) * float(column[i]),
                    str(JalaliDate(d[0], str(month) , d[2]))
                ]
                i +=1
                month +=1

            i = 0
        self.makeDataFrame(ret)
        return ret



    def opencsv(self):
        model_mali_csv = pandas.read_csv('model_mali.csv')
        print (type(model_mali_csv))
        df = pandas.DataFrame(model_mali_csv)
        return df

    def makeDataFrame(self , inputs):
        i = 0
        n = 0
        time = []
        columns = []
        init = []
        data_fin = {}
        for input in inputs:

            data_fin[input] = []
            while i < 29:
                if inputs[input][i][1] not in time:
                    time.append(inputs[input][i][1])
                init.append(inputs[input][i][0])
                data_fin[input].append(inputs[input][i][0])
                i += 1
            columns.append(str(input))
            i = 0
            # if n == 0:
            #     n = 1
        # print(data_fin)
        for input in inputs:
            i = len(data_fin[input])

            x = time.index(inputs[input][0][1])
            while n < x:
                data_fin[input].insert(0,0)
                n +=1
            n = 0
            x = time.index(inputs[input][28][1])
            x = abs(x - (len(time)-1))
            # print(x)
            while n <x:
                data_fin[input].append(0)
                n += 1
            n = 0

        dataframe_init = pandas.DataFrame(index=time , data = data_fin,columns=columns)
        print (dataframe_init)
        # print(time)
        # print(data_fin)
        # print(dataframe_init)
        # print (data_fin['hamin'])
        # INDEX IS DONE
        #COLUMNS ARE DONE










        # for input in inputs:
        # column = df.loc[0:29, str(gostare_data[0][2]) + "%"]
        # print (init)
        # df.insert(loc=time[0], column='hamin', value=init)

        # print(df.loc[time[0]:time[int(len(time))-1],columns[0]])