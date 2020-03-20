#
from bs4 import  BeautifulSoup
#
import urllib.request
# 1. 导入Python SSL处理模块
import ssl
#
import pymysql

import re
#
import  time

import  sched







def get_request_WGJS():

    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()

    url = 'https://quote.fx678.com/exchange/WGJS'

    headers = {
            # 'Host': 'www.vivino.com',
            # 'Connection': 'keep-alive',
            # 'Accept': 'application/json',
            # 'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
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

def get_request_SGE():

    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()

    url = 'https://quote.fx678.com/exchange/SGE'

    headers = {
            # 'Host': 'www.vivino.com',
            # 'Connection': 'keep-alive',
            # 'Accept': 'application/json',
            # 'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
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
        html = res_.read().decode('UTF-8')
        soup = BeautifulSoup(html, 'lxml')
        return soup
    except Exception as err:
        print(err)




def get_price_WGJS(soup):
    try:
        data= soup.find('table','market_tab_big foreign')
        return data
    except Exception as err:
        print(err)

def get_price_SGE(soup):
    try:
        data= soup.find('table','market_tab_big foreign')
        return data
    except Exception as err:
        print(err)



def return_fx678():

    try:
        fx678_data=[]

        res_SGE = get_request_SGE()

        soup_SGE = get_html(res_SGE)

        data_SGE = get_price_SGE(soup_SGE)

        #print(soup)

        for tr in data_SGE.findAll("tr"):
            datalist_SGE=[]
            for td in tr.findAll('td'):
                text = td.text.strip("\n").split(" ")
                #print(text)
                if text !=[''] and text !=['', ''] and text !=[]:
                    datalist_SGE.append(text[0])
            #print(datalist_SGE)

            if datalist_SGE !=[]:
                if datalist_SGE[0] in '黄金延期' or datalist_SGE[0] in '白银延期':
                    fx678_data.append(datalist_SGE)


        res_WGJS = get_request_WGJS()

        soup_WGJS = get_html(res_WGJS)

        data_WGJS = get_price_WGJS(soup_WGJS)

        # print(soup)

        for tr in data_WGJS.findAll("tr"):
            datalist_WGJS = []
            for td in tr.findAll('td'):
                text = td.text.strip("\n").split(" ")
                # print(text)
                if text != [''] and text != ['', ''] and text != []:
                    datalist_WGJS.append(text[0])
            #print(datalist_WGJS)

            if datalist_WGJS != []:
                if datalist_WGJS[0] in '现货黄金' or datalist_WGJS[0] in '现货白银':
                    fx678_data.append(datalist_WGJS)
        return fx678_data
    except Exception as err:
        print(err)
    # print(fx678_data)
    #
    # for data in fx678_data:
    #     print(data)


