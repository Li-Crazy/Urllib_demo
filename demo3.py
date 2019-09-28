#encoding: utf-8
import requests
from urllib import request
from urllib import parse
#request.Request类，增加请求头，解决反爬机制
start_url = "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC"
url = "https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
headers = {
    "Referer": "https://www.lagou.com/jobs/list_python?px=default&city=%E5%8C%97%E4%BA%AC",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400"
}

#拉钩网
data = {
    "first": "true",
    "pn": 1,
    "kd": "python"
}

res = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
response = request.urlopen(res)
print(response.read().decode('utf-8'))