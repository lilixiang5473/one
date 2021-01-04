# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 16:11
# @Author  : Game、北乐
# @Email   : Gamest@Foxmain.com
# @File    : 最新成交价.py

import requests

sum=1
while sum<400:
    s = requests.get(url="https://www.okex.me/api/spot/v3/instruments/BTC-USDT/ticker")
    data = "\n第【{}】条请求数据，请求时间为【{}】，最新成交价：【{}】\n".format(sum, s.json()["timestamp"], s.json()["last"])
    word_text=open(r'最新成交价数据.txt', 'a')
    word_text.write(data)
    word_text.close()
    sum+=1