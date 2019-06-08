from DB import *
import os
import werkzeug
from flask import Flask , jsonify
from flask_restful import Api, Resource, reqparse
from khayyam import *
from datetime import timedelta
from timeFunctions import khayam_type_days


class jaraem_taakhir_dar_bahre_bardari(Resource):
    # def get(self):
    #     parser = reqparse.RequestParser()
    #     parser.add_argument('gostare_id',required=True)
    #     args = parser.parse_args()
    #
    #
    #     mycursor.execute('select * from gostare where id = ' + args['gostare_id'])
    #     gostare_data = mycursor.fetchall()
    #     mycursor.execute ('select * from gostare_pishraft where gostare_id = '+str(gostare_data[0][0]))
    #     pishraft = mycursor.fetchall()
    #
    #     if pishraft and pishraft[0]:
    #         jarime_ghabl_az_shorooe_kar = (
    #                     50000 * int(khayam_type_days(gostare_data[0][3], pishraft[0][3])) * float(gostare_data[0][2]))
    #     else :
    #         return "no data for pishraft gostare"
    #         # jarime_ghabl_az_shorooe_kar = 0
    #     i = 0
    #     jame_kole_pishraft = 0
    #     while i < len(pishraft):
    #         jame_kole_pishraft = float(pishraft[i][2]) + jame_kole_pishraft
    #         print(i)
    #         i = i+1
    #
    #     dataye_return = {}
    #     i = 0
    #     # while i < 10:
    #     #     dataye_return[i] = {}
    #     #     dataye_return[i]['esme_gostare'] = gostare_data[0][1]
    #     #     dataye_return[i]['vazne_kole'] = gostare_data[0][2]
    #     #     dataye_return[i]['jame_kole_anjam_shode'] = jame_kole_pishraft
    #     #     dataye_return[i]['darsade_kare_baghi_mande'] = jame_kole_pishraft - gostare_data[0][2]
    #     #     dataye_return[i]['tarikh_barname_rizi_shode_bahre_bardari'] = gostare_data[0][3]
    #     #     dataye_return[i]['shorooe_bahre_bardari_az_pishraft_fiziki'] = pishraft[0][3]
    #     #     dataye_return[i]['tarikh_shorooe_ghest'] = "do mah bad az ghabli"
    #     #     dataye_return[i]['tarikh_shorooe_mohasebat_jarime'] = "se mah bad az ghabli"
    #     #     i = i + 1
    #     time_1 = gostare_data[0][3].split('-')
    #     time_1 = JalaliDate(time_1[0],time_1[1],time_1[2])
    #     # time2 = JalaliDate('1350', '01', '01')
    #     # # time = (time_1 - time2).days
    #     # print(time2.month)
    #     # time = timedelta(days= time)
    #     # print(time)
    #     retu = {}
    #     i = 0
    #     for pish in pishraft:
    #
    #         if i > 0:
    #             n = i -1
    #             time_1 = pishraft[n][3].split('-')
    #             time_1 = JalaliDate(time_1[0], time_1[1], time_1[2])
    #         d = pish[3].split('-')
    #         time = JalaliDate(d[0], d[1], d[2])
    #         days = (time - time_1).days
    #         retu[i] = {}
    #         retu[i]['jarime'] = (50000 * int(abs(days)) * float(gostare_data[0][2]))
    #         retu[i]['esme_gostare'] = gostare_data[0][1]
    #         retu[i]['vazne_kole'] = gostare_data[0][2]
    #         retu[i]['darsade_pishraft'] = int(pish[2])
    #         retu[i]['tarikh_pishraft'] = pish[3]
    #         if i>0:
    #             jame_kole_pishraft = jame_kole_pishraft + int(pish[2])
    #         else:
    #             jame_kole_pishraft = int(pish[2])
    #         retu[i]['jame_kole_anjam_shode'] = jame_kole_pishraft
    #         retu[i]['darsade_kare_baghi_mande'] = abs(jame_kole_pishraft - float(gostare_data[0][2]))
    #         retu[i]['tarikh_barname_rizi_shode_bahre_bardari'] = gostare_data[0][3]
    #         retu[i]['shorooe_bahre_bardari_az_pishraft_fiziki'] = pishraft[0][3]
    #         retu[i]['tarikh_shorooe_ghest'] = 'do mah bad az shorooe_bahre_bardari_az_pishraft_fiziki'
    #         retu[i]['tarikh_shorooe_mohasebat_jarime'] = "se mah bad az tarikh_shorooe_ghest"
    #         i = 1 + i
    #     mydb.commit()
    #     return retu
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gostare_id',required = True)
        parser.add_argument('darsad',required = True)
        parser.add_argument('tarikh_ghest_avaliye',required = True)
        parser.add_argument('tarikh_ghest_jariye',required = False)
        parser.add_argument('shomare_ghest',required = True)
        parser.add_argument('javab',required = True)
        args = parser.parse_args()

        sql = "INSERT INTO taakhir_dar_bahre_bardari (gostare_id,darsad , tarikh_ghest_avaliye , tarikh_ghest_jariye,shomare_ghest , javab) VALUES (%s ,%s, %s ,%s ,%s ,%s)"
        values = (args['gostare_id'],args['darsad'] , args['tarikh_ghest_avaliye'] , args['tarikh_ghest_jariye'],args['shomare_ghest'] , args['javab'])
        # TODO:: add gostare_id , darsad ,tarikh_ghest_avaliye , tarikh_ghest_jariye
        mycursor.execute(sql,values)
        mydb.commit()
        return True

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gostare_id')
        args = parser.parse_args()
        mycursor.execute('select * from taakhir_dar_bahre_bardari WHERE gostare_id = %s' , ( args['gostare_id'] ,))
        jarime_data = mycursor.fetchall()
        sql = ('select * from gostare where id = %s')
        mycursor.execute(sql ,( args['gostare_id'] ,))
        gostare = mycursor.fetchall()
        gostare = gostare[0]
        jadval = {}
        jadval['gostare'] = gostare[1]
        jadval['vazne_khat'] = gostare[2]
        jadval['tarikh_bahre_bardari'] = gostare[3]
        # TODO:: // name gostare , vazne_khat , tarikh_barnamehye , tarikh_bahre_bardari , tarikh_shorooe_ghest , tarikh_shorooe_daryaft_jarime

        # todo:: shomare_ghest , darsade_baghi_mande , tarikh_anjam_bahre_bardarfi  ,
        i = 0
        jarime_datas ={}
        jarime_datas['jadval_az_pish'] = jadval
        jarime_datas['n'] = {}
        while i < len(jarime_data):
            jarime_datas['n'][i]={}
            jarime_datas['n'][i]['shomare_ghest'] = jarime_data[i][5]
            jarime_datas['n'][i]['darsade_baghi_mande'] = jarime_data[i][2]
            jarime_datas['n'][i]['tarikh_anjam_bahre_bardarfi'] = jarime_data[i][4]
            i += 1
        i = 0
        list_ghests = []
        ape = []
        jarime_ghest_ghabl_az_avalin_kar= 0
        # ape.append([
        #     1
        # ])
        # ape.append([
        #     2
        # ])
        sum_jarime = 0
        while i < len(jarime_data):
            if i == 0:
                days_dif = khayam_type_days(jarime_data[i][3] ,gostare[3] )
                jarime_ghest_ghabl_az_avalin_kar = (50000 * int(abs(days_dif)) * float(jarime_data[i][2]))
                jarime_ghest= 0
            # if i > 0:
            #     days_dif = khayam_type_days(jarime_data[i][3], jarime_data[i-1][3])
            #     jarime_ghest = (50000 * int(abs(days_dif)) * float(jarime_data[i][2]))
            gostare_id = jarime_data[i][1]
            if jarime_data[i][5] == jarime_data[i-1][5] and i > 0:
                n = str(int(jarime_data[i][2]) + int(jarime_data[i-1][2]))
                days_dif = khayam_type_days(jarime_data[i][3], jarime_data[i - 1][3])
                jarime_ghest = (50000 * int(abs(days_dif)) * float(n))
                sum_jarime += jarime_ghest

                del ape[i-1]
                data = [
                gostare_id ,
                n ,
                jarime_data[i][3],
                jarime_data[i][4],
                jarime_data[i][5],
                jarime_data[i][6],
                sum_jarime
                ]
            else:
                n = jarime_data[i][2]
                days_dif = khayam_type_days(jarime_data[i][3], jarime_data[i - 1][3])
                jarime_ghest = (50000 * int(abs(days_dif)) * float(n))
                sum_jarime += jarime_ghest
                data = [
                gostare_id ,
                n ,
                jarime_data[i][3],
                jarime_data[i][4],
                jarime_data[i][5],
                jarime_data[i][6],
                sum_jarime
                ]
            ape.append(data)
            # ape[i].append(jarime_data[i][4])
            # ape[i].append(jarime_data[i][5])
            # ape[i].append(jarime_data[i][6])

            i +=1
        mydb.commit()
        jarime_datas['jadval_az_pish']['jarime_az_ghabl_az_karkard']=jarime_ghest_ghabl_az_avalin_kar

        jarime_datas['list'] = ape
        return jarime_datas
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('shomare_ghest',required=True)
        parser.add_argument('gostare_id',required = True)
        args = parser.parse_args()
        sql = ('delete from taakhir_dar_bahre_bardari where shomare_ghest = %s and gostare_id=%s')
        value = (args['shomare_ghest'],args['gostare_id'])
        mycursor.execute(sql , value)
        mydb.commit()
        return True