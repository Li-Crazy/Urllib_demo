#encoding: utf-8

from urllib import request
from http.cookiejar import MozillaCookieJar#保存cookie到本地

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)#加载cookie，传递filename,上面已经传递了就不用了
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)
resp = opener.open("http://httpbin.org/cookies")
for cookie in cookiejar:
    print(cookie)
# cookiejar.save(ignore_discard=True)#ignore_discard=True保存即将过期即将丢弃的cookie
