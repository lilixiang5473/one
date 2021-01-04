# 利用有道词典翻译内容

import urllib.request
import urllib.parse
import json

def translate(words):
    targetURL = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
    data = {}
    data['type'] = 'AUTO'
    data['i'] = words
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.8'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['action'] = 'FY_BY_CLICKBUTTON'
    data['typoResult'] = 'true'
    #将自定义data转换成标准格式
    data = urllib.parse.urlencode(data).encode('utf-8')
    #发送用户请求
    html = urllib.request.urlopen(targetURL, data)
    #读取并解码内容
    rst = html.read().decode("utf-8")
    rst_dict = json.loads(rst)
    return rst_dict['translateResult'][0][0]['tgt']

if __name__ == "__main__":
    print("输入字母q表示退出")
    while True:
        words = input("请输入要查询的单词或句子:\n")
        if words == 'q':
            break
        result = translate(words)
        print("翻译结果是：%s"%result)
