#
import pymysql
#
import  time

import GetPrice_fx678

import GetPrice_ICBC

import GetPrice_investing

import multiprocessing
from multiprocessing import Process

from threading import  Timer



# 创建连接
#db = pymysql.connect(host='', port=3306,user='root', password='', db='mydata', charset='utf8')
db = pymysql.connect(host='', port=3306,user='root', password='', db='mydata', charset='utf8')
# 创建游标对象
cursor = db.cursor()


def insrt_mysql_ag(data):
    try:
        if len(data):
            #print(data)
            cursor.execute(
                'insert into price_icbc_ag_time(ag_mr,ag_mc,ag_zj,get_time)values(%s,%s,%s,%s)',
                data)
            db.commit()
    except Exception as err:
        print(err)



def insrt_mysql_inversting(data):
    try:
        if len(data):
            #print(data)
            cursor.execute(
                'insert into price_silver_time(price_silver,get_time,tag_time,tag_info,tag_cfd,tag_usd,tag_money)values(%s,%s,%s,%s,%s,%s,%s)',
                data)
            db.commit()
        time.sleep(60)
    except Exception as err:
        print(err)

def insrt_mysql_fx678_silver(data):
    try:
        if len(data):
            #print(data)
            cursor.execute(
                'insert into price_silver(price_silver_new,price_silver_fdjg,price_silver_fdbfb,price_silver_zg,price_silver_zd,price_silver_zrsp,price_silver_sj,price_silver_time,price_silver_day)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                data)
            db.commit()
    except Exception as err:
        print(err)

def insrt_mysql_fx678_god(data):
    try:
        if len(data):
            #print(data)
            cursor.execute(
                'insert into price_god(price_god_new,price_god_fdjg,price_god_fdbfb,price_god_zg,price_god_zd,price_god_zrsp,price_god_sj,price_god_time,price_god_day)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                data)
            db.commit()
    except Exception as err:
        print(err)

def insrt_mysql_fx678_ag(data):
    try:
        if len(data):
            #print(data)
            cursor.execute(
                'insert into price_ag(price_ag_new,price_ag_fdjg,price_ag_fdbfb,price_ag_zg,price_ag_zd,price_ag_zrsp,price_ag_sj,price_ag_time,price_ag_day)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                data)
            db.commit()
    except Exception as err:
        print(err)

def insrt_mysql_fx678_au(data):
    try:
        if len(data):
            #print(data)
            cursor.execute(
                'insert into price_au(price_au_new,price_au_fdjg,price_au_fdbfb,price_au_zg,price_au_zd,price_au_zrsp,price_au_sj,price_au_time,price_au_day)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                data)
            db.commit()
    except Exception as err:
        print(err)

def inset_mysql_icbc_process():
    while True:
        try:
            icbc_data = GetPrice_ICBC.return_icbc()
            print(icbc_data)
            if icbc_data[1] not in '0.00':
                insrt_mysql_ag(icbc_data)
            print("-------------")
            time.sleep(60)
        except Exception as err:
            print(err)



def inset_mysql_fx678_process():

    while True:
        try:
            fx678_data = GetPrice_fx678.return_fx678()
            get_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
            get_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

            for data in fx678_data:
                if '黄金延期' in data:
                    del data[0]
                    data.append(get_time)
                    data.append(get_day)
                    insrt_mysql_fx678_au(data)
                    print(data)
                else:
                    if '白银延期' in data:
                        del data[0]
                        data.append(get_time)
                        data.append(get_day)
                        insrt_mysql_fx678_ag(data)
                        print(data)
                    else:
                        if '现货黄金' in data:
                            del data[0]
                            data.append(get_time)
                            data.append(get_day)
                            insrt_mysql_fx678_god(data)
                            print(data)
                        else:
                            if '现货白银' in data:
                                del data[0]
                                data.append(get_time)
                                data.append(get_day)
                                insrt_mysql_fx678_silver(data)
                                print(data)
            print("-------------")
            time.sleep(60)

        except Exception as err:
            print(err)

def inset_mysql_investing_process():

    while True:
        try:

            re_=GetPrice_investing.get_request()
            soup=GetPrice_investing.get_html(re_)
            in_data=GetPrice_investing.get_price(soup)
            in_tag=GetPrice_investing.get_tag(soup)

            print(in_data)
            print(in_tag)
            time.sleep(60)

        except Exception as err:
            print(err)



if __name__ == '__main__':

    icbc_process=Process(target=inset_mysql_icbc_process)
    icbc_process.daemon=False
    icbc_process.start()


    fx678_process=Process(target=inset_mysql_fx678_process)
    fx678_process.daemon=False
    fx678_process.start()

    # investing_process=Process(target=inset_mysql_investing_process)
    # investing_process.daemon=False
    # investing_process.start()


    print(icbc_process.pid)

    print(fx678_process.pid)




