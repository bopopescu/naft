from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
from khayyam import *
from datetime import timedelta
from timeFunctions import khayam_type_days


class jaraem_taakhir_dar_bahre_bardari(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gostare_id',required=True)
        args = parser.parse_args()

        mycursor.execute('select * from gostare where id = ' + args['gostare_id'])
        gostare_data = mycursor.fetchall()
        mycursor.execute ('select * from gostare_pishraft where gostare_id = '+str(gostare_data[0][0]))
        pishraft = mycursor.fetchall()
        if pishraft:
            jarime_ghabl_az_shorooe_kar = (
                        50000 * int(khayam_type_days(gostare_data[0][3], pishraft[0][3])) * float(gostare_data[0][2]))
        else :
            jarime_ghabl_az_shorooe_kar = 0
        i = 0
        jame_kole_pishraft = 0
        while i < len(pishraft):
            jame_kole_pishraft = float(pishraft[i][2]) + jame_kole_pishraft
            print(i)
            i = i+1

        dataye_return = {}
        i = 0
        # while i < 10:
        #     dataye_return[i] = {}
        #     dataye_return[i]['esme_gostare'] = gostare_data[0][1]
        #     dataye_return[i]['vazne_kole'] = gostare_data[0][2]
        #     dataye_return[i]['jame_kole_anjam_shode'] = jame_kole_pishraft
        #     dataye_return[i]['darsade_kare_baghi_mande'] = jame_kole_pishraft - gostare_data[0][2]
        #     dataye_return[i]['tarikh_barname_rizi_shode_bahre_bardari'] = gostare_data[0][3]
        #     dataye_return[i]['shorooe_bahre_bardari_az_pishraft_fiziki'] = pishraft[0][3]
        #     dataye_return[i]['tarikh_shorooe_ghest'] = "do mah bad az ghabli"
        #     dataye_return[i]['tarikh_shorooe_mohasebat_jarime'] = "se mah bad az ghabli"
        #     i = i + 1
        time_1 = pishraft[0][3].split('-')
        time_1 = JalaliDate(time_1[0],time_1[1],time_1[2])
        # time2 = JalaliDate('1350', '01', '01')
        # # time = (time_1 - time2).days
        # print(time2.month)
        # time = timedelta(days= time)
        # print(time)
        retu = {}
        for pish in pishraft:
            d = pish[3].split('-')
            time = JalaliDate(d[0], d[1], d[2])
            days = (time - time_1).days
            retu[pish[0]] = {}
            retu[pish[0]]['jarime'] = (50000 * int(abs(days)) * float(gostare_data[0][2]))
            retu[pish[0]]['esme_gostare'] = gostare_data[0][1]
            retu[pish[0]]['vazne_kole'] = gostare_data[0][2]
            retu[pish[0]]['jame_kole_anjam_shode'] = jame_kole_pishraft
            retu[pish[0]]['darsade_kare_baghi_mande'] = jame_kole_pishraft - float(gostare_data[0][2])
            retu[pish[0]]['tarikh_barname_rizi_shode_bahre_bardari'] = gostare_data[0][3]
            retu[pish[0]]['shorooe_bahre_bardari_az_pishraft_fiziki'] = pishraft[0][3]
            retu[pish[0]]['tarikh_shorooe_ghest'] = "do mah bad az ghabli"
            retu[pish[0]]['tarikh_shorooe_mohasebat_jarime'] = "se mah bad az ghabli"
        return retu
