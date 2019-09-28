#encoding: utf-8

from urllib import request#request存放网络请求相关的
from urllib import parse

#urlopen的用法，爬取网页代码
response = request.urlopen('http://www.baidu.com')
# print(response.read())
print(response.read(10))
print(response.readline())
print(response.readlines())
print(response.getcode())

#urlretrieve的用法，保存网页文件
request.urlretrieve('http://www.baidu.com','baidu.html')
request.urlretrieve('https://i03picsos.sogoucdn.com/0c8b055dae07a16f','yangjian.jpg')



#urlencode函数的用法，把字典文件转换为URL编码的数据
params1 = {'name':'wangxiaoxiao', 'age':18, 'greet':'Hello World!'}
result = parse.urlencode(params1)
print(result)
# url = "http://www.baidu.com/s?wd=刘德华"
url = "http://www.baidu.com/s"
params2 = {'wd':'刘德华'}
qs = parse.urlencode(params2)
print(qs)
url = url + "?" + qs
resq = request.urlopen(url)
print(resq.read())

#parse_qs函数的用法，对编码后的URL解码
params1 = {'name':'wangxiaoxiao', 'age':18, 'greet':'Hello World!'}
result1 = parse.urlencode(params1)
print(result1)
result2 = parse.parse_qs(result1)
print(result2)

