# import urllib.request
# import socket
# import urllib.error
# # import urllib.parse
# # response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# # print(response.getcode)
# # print(response.getheaders())
# # print(response.getheader('Server'))
#
#
# # data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding = 'utf8')
# try:
#     response = urllib.request.urlopen('http://httpbin.org/post',timeout =0.01)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('Time out!')
# # print(response.read())


# import urllib.request
#
# request = urllib.request.Request("http://www.baidu.com")
# response = urllib.request.urlopen(request)
# print(response.read().decode("utf-8"))


# from urllib import request,parse
# url = "http://httpbin.org/post"
# headers = {
#     #伪装一个火狐浏览器
#     "User-Agent":'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)',
#     "host":'httpbin.org'
# }
# dict = {
#     "name":'Germey'
# }
# data = bytes(parse.urlencode(dict),encoding = "utf8")
# req = request.Request(url = url,data =data,headers=headers,method = "POST")
# # req.add_header('User-Agent',:'Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)')
# response = request.urlopen(req)
# print(response.read().decode("utf-8"))


# import urllib.request
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm = 'PDQ Application',
#                           uri = 'http://mahler:8092/site-updates.py',
#                           user = 'klem',
#                           passwd = 'kadidd!ehopper')
# opener = urllib.request.build_opener(auth_hander)
# urllib.request.install_opener(opener)
# urllib.request.urlopen('http://www.example.com/login.html')

#opener 使用方法
# import urllib.request
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='PDQ Application',
#                           uri='https://mahler:8092/site-updates.py',
#                           user='klem',
#                           passwd='kadidd!ehopper')
# opener = urllib.request.build_opener(auth_handler)
# urllib.request.install_opener(opener)
# urllib.request.urlopen('http://www.example.com/login.html')


# #ProxyHandler 使用方法
# import urllib.request
# proxy_handler = urllib.request.ProxyHandler({
#     'http':'http://218.202.111.10:80',
#     'https':'https://180.250.163.34:8888'
# })
# opener = urllib.request.build_opener(proxy_handler)
# response = opener.open('https://www.baidu.com')
# print(response.read())


# #Cookie 设置
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

#cookie输出为文件
import http.cookiejar,urllib.request
filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)


#LWPCookieJar
cookie = http.cookiejar.LWPCookieJar()
cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
print(response.read().decode('utf-8'))




