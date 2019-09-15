# encoding:utf8
from interface.inter import *
import inspect

http = HTTP()
func = getattr(http,'get')
func('http://192.168.111.129:8080/inter/HTTP//auth')
args = inspect.getfullargspec(func).__str__()
print(args)
args =  args[args.find('args=')+5:args.rfind(', varargs')]
args = eval(args)

args.remove('self')
print(args)






