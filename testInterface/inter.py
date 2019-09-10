# encoding:utf8
import requests,json

class HTTP:

    def __init__(self):
        self.session = requests.session()
        self.result = ''
        self.jsonres = {}
        # 用来保存关联的字典
        self.params ={}
        self.token=''

    def post(self,url,d=None,j=None,header=None,en='utf8'):
        if d is None:
            pass
        else:
            d= self.__get_data(d)
        res=self.session.post(url,d,j)
        self.result = res.content.decode(en)
        self.jsonres = json.loads((self.result))

    def addheader(self,key,value):
        # value=self.__get_param(value)
        self.session.headers[key]=value

    def assertequals(self,key,value):
        if str(self.jsonres[key])==str(value):
            print('PASS')
        else:
            print('FAIL')

    def savejson(self,key,p):
        self.params[p]=self.jsonres[key]
        self.token=self.params[p]
        return self.token

    # def savejsons(self, key, p):
    #     self.params[p] = self.jsonres[key]

    def __get_param(self,s):
        #按规则获取关联的参数
        s = ''
        for key in self.params:
            s=s.replace('{'+key+'}',self.params[key])

        return s

    def __get_data(self,s):
        s=eval(s)
        return s

    def __get_dict(self,s):
        param={}
        s=''
        p=s.split('&')
        for pp in p:
            ppp=pp.split('=')
            param[ppp[0]]=ppp[1]

        print(param)
        return param




