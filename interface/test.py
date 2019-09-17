# encoding:utf8
from interface.inter import *
import inspect

http = HTTP()
# 反射制定调用函数
func = getattr(http,'post')
func('http://192.168.2.102:8080/inter/HTTP//auth')
# 获取调用函数的参数个数
args = inspect.getfullargspec(func).__str__()
print(args)
# 获取指定参数  find
args =  args[args.find('args=')+5:args.rfind(', varargs')]
print(args)
print(type(args))
# 转换成list
args = eval(args)

args.remove('self')
print(args)






