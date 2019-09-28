#encoding: utf-8
#开心网登录URL：http://www.kaixin001.com/login/
#个人主页：http://www.kaixin001.com/home/?uid=181846492
from urllib import request
from http.cookiejar import CookieJar
from urllib import parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3650.400 QQBrowser/10.4.3341.400"
}

def get_opener():
    #1.登录
    #1.1.创建一个cookiejar对象
    cookiejar = CookieJar()
    #1.2.使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    #1.3.使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    return opener

def login_renren(opener):
    #1.4.使用opener发送登录请求（人人网的邮箱和密码）
    data = {
        "email":"18854889585",
        "password":"1234567890"
    }
    login_url = "http://www.renren.com/SysHome.do"
    req = request.Request(url=login_url,headers=headers,data=parse.urlencode(data).encode('utf-8'))
    resp = opener.open(req)
    with open('ren.html', 'w', encoding='utf-8') as f:
        f.write(resp.read().decode('utf-8'))
# def visit_profile(opener):
#      #2.访问个人主页
#     zhuye_url = 'http://www.renren.com/259452569/profile'
#     #获取个人主页的页面时，使用之前的opener，不用新建，已经包含了cookie信息
#     req = request.Request(url=zhuye_url,headers=headers)
#     resp = opener.open(req)
#     with open('renren.html','w',encoding='utf-8') as f:
#         f.write(resp.read().decode('utf-8'))

if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    # visit_profile(opener)