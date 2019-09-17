# encoding:utf8
from interface.inter import HTTP

http=HTTP()

#获取token
http.post('http://192.168.2.102:8080/interface/HTTP//auth')
http.assertequals('status','200')
http.savejson('token','t')
http.addheader('token','{t}')
print(http.session.headers)

#登录接口
http.post('http://192.168.2.102:8080/interface/HTTP/login',d="username=Will&password=123456")

http.assertequals('status','200')
print(http.result)

#查询用户信息
http.savejson('userid','userid')
http.post('http://192.168.2.102:8080/interface/HTTP/getUserInfo',d="id={userid}")
http.assertequals('status','200')
print(http.result)

#注销用户
http.post('http://192.168.2.102:8080/interface/HTTP/logout')
http.assertequals('status','200')
print(http.result)
