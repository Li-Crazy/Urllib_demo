#encoding: utf-8

from urllib import request

#未使用代理
# url = "http://httpbin.org/ip"
# resp = request.urlopen(url)
# print(resp.read())

#使用代理
url = "http://httpbin.org/ip"
#1.使用ProxyHandler,传入代理构建一个handler
handler = request.ProxyHandler({"http":"221.11.105.68:56120"})
#2.使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
#3.使用opener去发送一个请求
response = opener.open(url)
print(response.read())
"""  
ProxyHandler处理器 (代理) :
1.代理的原理:在请求目的网站之前，先请求代理服务器，然后让代理服务器去请求目的网站，代理服务器拿到目的网站的
            数据后，再转发给我们的代码。
2. http://httpbin.org: 这个网站可以方便的查看http请求的一些参数。
3.在代码中使用代理:
    *使用"urllib.request.ProxyHandler"，传入一个代理，这个代理是一个字典，字典的key依赖于代理服务器能够接收
    的类型，一般是"http"或者"https"，值是"ip:port"。
    *使用上一步创建的"handler"， 以及"request.build_opener"创建一个"opener"对象。
    *使用上一步创建的"opener"，调用"open"函数， 发起请求。
"""