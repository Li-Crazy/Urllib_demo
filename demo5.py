#encoding: utf-8
#开心网登录URL：http://www.kaixin001.com/login/
#个人主页：http://www.kaixin001.com/home/?uid=181846492

from urllib import request
#1.不使用cookie去请求大鹏主页
#不管有没有反爬机制都加上请求头
dapeng_url = "http://www.kaixin001.com/home/?uid=181846492"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400",
     "Cookie": "_ref=5cac71966489b; _cpmuid=1336587256; SERVERID=_srv80-122_; _vid=C866A4E958200001EC"
               "3D29108DC01C94; __gads=ID=8b3731fe52838b32:T=1554805143:S=ALNI_MZBOY4qjWk4BvjaDmQPrY4b"
               "EYdEUQ; _reg_src=qq_daohang_; _user=ba37d38ce9ecee21967872d4862599de_181846492_1554805"
               "310; _preemail=18854889585; noFocusContent=1; onlinenum=c%3A0; wpresence=jZH6EPHtCXJTHw"
               "Eythv5avPwEp15CfwUXKxyYA.ZGZ0MTgxODQ2NDky"
}
req = request.Request(url=dapeng_url,headers=headers)
resp = request.urlopen(req)
# print(resp.read().decode('utf-8'))
with open('kaixin.html','w',encoding='utf-8') as f:
    #write函数必须写入一个str数据类型
    #resp.read()读出的是一个bytes数据类型
    #bytes -->decode解码 -->str
    #str -->encode编码 -->bytes
    f.write(resp.read().decode('utf-8'))