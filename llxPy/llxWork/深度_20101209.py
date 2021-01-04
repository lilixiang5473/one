# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 16:08
# @Author  : Game、北乐
# @Email   : Gamest@Foxmain.com
# @File    : 深度列表.py




import requests
import time


sum=1
while sum<400:
    url = "https://www.okex.me/api/spot/v3/instruments/BTC-USDT/book?depth=&size=50"
    s = requests.get(url)
    data= "\n第【{}】条请求数据，请求时间为【{}】\n返回卖家数据：{}\n返回买家数据：{}\n".format(sum, s.json()["timestamp"], s.json()["asks"], s.json()["bids"])
    word_text=open(r'深度列表数据.txt', 'a')
    word_text.write(data)
    word_text.close()
    sum+=1
