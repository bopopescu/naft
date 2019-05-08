from datetime import datetime , date
def jarime(dore_ghable , nerkh_jarime , tarikh_khod , tarikh_ghabl):
    # TODO:: have to complete this and i am sleepy and cant do it
    return ekhtelaf_rooz()
from khayyam import *
def khayyam_time_sort(date):
    d = date.split('-')
    time = JalaliDate(d[0],d[1],d[2])
    time2 = JalaliDate('1350','01','01')
    return (time - time2).days
def khayam_type(date1, date2):
    d1 = date1.split('-')
    d2 = date2.split('-')
    time = JalaliDate(d1[0], d1[1], d1[2])
    time1 = JalaliDate(d1[0], d1[1], d1[2])
    time2 = JalaliDate(d2[0], d2[1], d2[2])
    time = time - time2
    days = abs(int(time.days))
    return days / int(time1.daysinmonth)
def ekhtelaf_rooz(datee1 , datee2):
    sal = {}
    sal[1] = 31
    sal[2] = 31
    sal[3] = 31
    sal[4] = 31
    sal[5] = 31
    sal[6] = 31
    sal[7] = 30
    sal[8] = 30
    sal[9] = 30
    sal[10] = 30
    sal[11] = 30
    sal[12] = 29
    date1 = datee1
    date2 = datee2
    date1 = date1.split('/')
    date2 = date2.split('/')
    if float(date1[0]) - float(date2[0]) == 0:
        roozHa = float(date1[2]) - float(sal[float(date1[1])])
        roozHa = abs(roozHa)
        if float(date1[1]) - float(date2[1]) == 0:
            rooHamoonMah = float(date2[2]) - float(sal[float(date2[1])])
            roozHa = roozHa - abs(rooHamoonMah)
            return roozHa
        roozHa = roozHa + float(date2[2])
        mah = float(date1[1]) - float(date2[1])
        mah = abs(mah)
        # return mah
        mah_shomar = float(date1[2])
        if mah != 0:
            for i in range(mah):
                roozHa = roozHa + float(sal[float(mah_shomar)])
                mah_shomar = mah_shomar + 1
                if mah_shomar == 12:
                    mah_shomar = 1
        return roozHa
    if abs(float(date1[0]) - float(date2[0])) != 0:
        roozHa = float(date1[2]) - float(sal[float(date1[1])])
        roozHa = abs(roozHa)
        roozHa = roozHa + float(date2[2])
        dateee1 = datetime.strptime((datee1) , '%Y/%m/%d')
        dateee2 = datetime.strptime((datee2) , '%Y/%m/%d')
        from dateutil import relativedelta
        diffs = relativedelta.relativedelta(dateee1, dateee2)
        mah = abs(diffs.months)
        print(mah)
        mah = mah +  abs(float(diffs.months))
        print(mah)
        mah = mah + (abs(diffs.years) * 12 )
        mah_shomar = float(date1[2])
        if mah != 0:
            for i in range(mah):
                roozHa = roozHa + float(sal[float(mah_shomar)])
                mah_shomar = mah_shomar + 1
                if mah_shomar == 12:
                    mah_shomar = 1
        return roozHa

