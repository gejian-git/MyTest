# encoding:utf8
from common.Excel import *
from interface import *
import inspect
from interface.inter import HTTP

http =HTTP()
reader = Reader()
reader.open_excel('../lib/cases/HTTP接口用例.xls')
sheetname = reader.get_sheets()