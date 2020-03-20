#
from bs4 import  BeautifulSoup
#
import urllib.request
# 1. 导入Python SSL处理模块
import ssl

import re
#
import  time

def get_request():

    # 2. 表示忽略未经核实的SSL证书认证
    context = ssl._create_unverified_context()

    url = 'https://mybank.icbc.com.cn/icbc/newperbank/perbank3/frame/frame_index.jsp?servicdId=PBL200603'

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
        html = res_.read().decode('GBK')

        soup = BeautifulSoup(html, 'lxml')

        #print(soup)
        return html
    except Exception as err:
        print(err)



def get_price_AG(soup):
    try:

        tag_info1 = re.findall('jQuery.*uint1[5,6,7]_acgold.*text.*[0-9].[0-9].*',soup)
        get_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

        AG_MR = tag_info1[3].strip('jQuery("#uint15_acgold").text("').strip('");')
        AG_MC = tag_info1[4].strip('jQuery("#uint16_acgold").text("').strip('");')
        AG_ZJ = tag_info1[5].strip('jQuery("#uint17_acgold").text("').strip('");')

        price_info_ag =[AG_MR,AG_MC,AG_ZJ,get_time]
        return price_info_ag
    except Exception as err:
        print(err)


def return_icbc():
    try:

        g_res = get_request()

        g_soup = get_html(g_res)

        price_info_ag = get_price_AG(g_soup)

        return price_info_ag
    except Exception as err:
        print(err)



