# encoding:utf8
import requests,json,traceback

class HTTP:

    def __init__(self,writer):
        self.session = requests.session()
        self.result = ''
        self.jsonres = {}
        # 用来保存关联的字典
        self.params ={}
        self.url =''
        self.writer = writer

    def seturl(self,u):
        if u.startswith('http') or u.startswith('https'):
            self.url=u
            self.writer.write(self.writer.row,7,'PASS')
            self.writer.write(self.writer.row,8,str(self.url))

        else:
            print('Error:URL格式有误')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, 'URL格式有误')


    def post(self,url,d=None,en=''):
        #设置请求的url信息
        if not(url.startswith('http') or url.startswith('https')):
            url=self.url + '/' + url

        if d is None or d == '':
            pass
        else:
            d= self.__get_param(d)
            d= self.__get_data(d)

        if en == '' or en == ' ':
            en = 'utf8'

        #如果返回有ssl，需要加上verify=False
        res=self.session.post(url,d,verify=False)
        self.result = res.content.decode(en)
        try:
            self.jsonres = json.loads((self.result))
            self.writer.write(self.writer.row,7,'PASS')
            self.writer.write(self.writer.row,8,str(self.jsonres))
        except:
            self.jsonres={}
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))

    def removeheader(self,key):
        """
        从头里面删除一个键
        :param key:
        :return:
        """
        try:
            self.session.headers.pop(key)
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.session.headers))
        except:
            print('没有'+key+'这个键对应的值存在')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.session.headers))

    def addheader(self,key,value):
        value=self.__get_param(value)
        self.session.headers[key]=value
        self.writer.write(self.writer.row, 7, 'PASS')
        self.writer.write(self.writer.row, 8, str(self.session.headers))


    def assertequals(self,key,value):
        value = self.__get_param(value)
        res = str(self.result)
        try:
            res = str(self.jsonres[key])
        except:
            print('参数取值有误')
        if res==str(value):
            print('PASS')
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.result))
        else:
            print('FAIL')
            self.writer.write(self.writer.row, 7, 'FAIL')
            self.writer.write(self.writer.row, 8, str(self.result))

    def savejson(self,key,p):
        try:
            self.params[p]=self.jsonres[key]
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.params[p]))
        except Exception as e:
            print('保存参数失败')
            print(traceback.format_exc())
            self.writer.write(self.writer.row, 7, 'PASS')
            self.writer.write(self.writer.row, 8, str(self.jsonres))


    def getdata(self,s):
        s=eval(s)
        return s

    def __get_param(self,s):
        #按规则获取关联的参数
        for key in self.params:
            s=s.replace('{'+key+'}',str(self.params[key]))

        return s

    # def __get_data(self,s):
    #     s=eval(s)
    #     return s

    def __get_data(self,s):
        param={}
        p=s.split('&')
        for pp in p:
            ppp=pp.split('=')
        #异常处理
            try:
                param[ppp[0]]=ppp[1]
            except Exception as e:
                print('Waring:Url格式不标准')

        print(param)
        return param




