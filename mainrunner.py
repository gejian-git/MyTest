# encoding:utf8
"""
    自动化主入口
"""
from common.Excel import *
from interface import *
import inspect
from interface.inter import HTTP
import os, xlrd
from xlutils.copy import copy
"""
这是整个自动化框架的主入口：

"""

def runcase(line,f):
    #分组信息不用执行
    if len(line[0])>0 or len(line[1])>0:
        return
    #反射获取关键字函数
    func = getattr(f, line[3])
    # 获取参数列表
    args = inspect.getfullargspec(func).__str__()
    args = args[args.find('args=') + 5:args.rfind(', varargs')]
    args = eval(args)
    args.remove('self')
    # print(args)
    # 不接收参数的调用
    if len(args)==0:
        func()
        return

    if len(args)==1:
        func(line[4])
        return

    if len(args)==2:
        func(line[4],line[5])
        return

    if len(args)==3:
        func(line[4],line[5],line[6])
        return

    print('Warning:目前只支持3个参数的关键字')


reader = Reader()
reader.open_excel('./lib/cases/HTTP接口用例.xls')
sheetname = reader.get_sheets()


writer = Writer()
writer.copy_open('./lib/cases/HTTP接口用例.xls', './lib/cases/result-HTTP接口用例.xls')

http =HTTP(writer)
for sheet in sheetname:
    # 设置当前读取的sheet页面
    reader.set_sheet(sheet)
    #保持读写同一个sheet
    writer.set_sheet(sheet)
    for i in range(reader.rows):
        writer.row=i
        line = reader.readline()
        # print(line)
        runcase(line,http)

writer.save_close()







