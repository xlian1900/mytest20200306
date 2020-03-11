#
from bs4 import  BeautifulSoup
#
import urllib.request
# 1. 导入Python SSL处理模块
import ssl
#
import pymysql
#
import  time

import  sched

# 创建连接
#db = pymysql.connect(host='', port=3306,user='root', password='', db='', charset='utf8')
db = pymysql.connect(host='', port=3306,user='root', password='', db='', charset='utf8')
# 创建游标对象
cursor = db.cursor()

def insrt_mysql(date):
    try:
        if len(date):
            cursor.execute(
                'insert into price_silver_time(price_silver,get_time,tag_info) values(%s,%s,%s)',
                date)
            db.commit()
    except Exception as err:
        print(err)





def get_request():

    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()

    url = 'https://cn.investing.com/commodities/silver'

    headers = {
            # 'Host': 'www.vivino.com',
            # 'Connection': 'keep-alive',
            # 'Accept': 'application/json',
            # 'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
            # 'Content-Type': 'application/json',
            # 'Referer': ' ',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh,zh-CN;q=0.9,en;q=0.8',
            # 'Cookie': '',
            # 'If-None-Match': 'W/"ab73c8aecbc35e1ac6d17806bf5a1c49"',
    }



    try:
        # url 作为Request()方法的参数，构造并返回一个Request对象
        request = urllib.request.Request(url, headers=headers)
        # Request对象作为urlopen()方法的参数，发送给服务器并接收响应
        res_ = urllib.request.urlopen(request, context=context)
        # 在urlopen()方法里 指明添加 context 参数
        return res_
    except Exception as err:
        print(err)



def get_html(res_):

    try:
        html = res_.read().decode('utf-8')

        soup = BeautifulSoup(html, 'lxml')

        #print(soup)
        return soup
    except Exception as err:
        print(err)


def get_price(soup):
    try:
        tag = soup.find('fieldset')
        price = tag.find('input')["value"]
        get_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        tag_info = soup.find(name='div', attrs='bottom lighterGrayFont arial_11').text.strip("\n").strip("( 免责声明 )")

        date = [price, get_time, tag_info]

        return date
    except Exception as err:
        print(err)


def get_tag(soup):
    try:

        tag_info = soup.find(name='div', attrs='bottom lighterGrayFont arial_11').text.strip("\n").strip("( 免责声明 )")

        return tag_info
    except Exception as err:
        print(err)


if __name__ == '__main__':

    while True:
        try:
            res_ = get_request()

            soup = get_html(res_)

            date = get_price(soup)

            tag_info=get_tag(soup)
            # print(date)
            # print(tag_info)

            sta_tag = '实时数据' in tag_info
            if('实时数据' in tag_info):
                insrt_mysql(date)
        except Exception as err:
            print(err)

    time.sleep(100)

