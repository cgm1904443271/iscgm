# 封装请求类
from urllib.parse import parse_qs

class MyRequest:
    def __init__(self,environ,start_response):
        self.start_response = start_response
        self.environ = environ

        # 请求方法
        self.method = environ.get('REQUEST_METHOD','GET')
        # 请求路径
        self.path = environ.get('PATH_INFO','/')

        # cookie
        # print(environ.get('HTTP_COOKIE',''))
        # print()
        self.cookies = environ.get('HTTP_COOKIE','').split(";")
        # print(self.cookies)
        self.cookies = [value.strip().split('=') for value in self.cookies]
        # print(self.cookies)
        self.cookies = {key:value for key,value in self.cookies}
        # print(self.cookies)

        #get参数
        self.GET = self.get_parameters()

        # post参数字典
        self.POST = self.post_para()

    # 获取get参数
    def get_parameters(self):
        queryString = self.environ.get('QUERY_STRING','')
        data = parse_qs(queryString)
        """
        {'username':['admin']}
        """
        for key in data:
            if len(data[key]) == 1:
                data[key] = data[key][0]
        return data

    def post_para(self):
        # 请求参数长度
        try:
            contentlength = int(self.environ.get('CONTENT_LENGTH', 0))
        except Exception as e:
            contentlength = 0

        fp = self.environ.get('wsgi.input')
        data = fp.read(contentlength)
        data =  parse_qs(data.decode('utf-8'))
        for key in data:
            if len(data[key]) == 1:
                data[key] = data[key][0]
        return data