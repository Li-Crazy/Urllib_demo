#encoding: utf-8

from urllib import parse

#urlparse解析url,有params属性
url = 'http://www.baidu.com/s;hello?wd=python&username=abc#1'
result = parse.urlparse(url)
print(result)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('params:',result.params)
print('query:',result.query)
print('fragment:',result.fragment)

#urlsplit解析url,无params属性
url = 'http://www.baidu.com/s;hello?wd=python&username=abc#1'
result1 = parse.urlsplit(url)
print(result1)
print('scheme:',result1.scheme)
print('netloc:',result1.netloc)
print('path:',result1.path)
print('query:',result1.query)
print('fragment:',result1.fragment)