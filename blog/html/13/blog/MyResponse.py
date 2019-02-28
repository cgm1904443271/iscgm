# 自己封装响应类
from settings import *
import jinja2
class MyResponse:
    def __init__(self,request):
        self.request = request;
        self.status = "200 ok"
        self.headers = []
    def load(self,file,**kwargs):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES))
        template = env.get_template(file)
        self.headers.append(('Content-Type', 'text/html'))
        self.request.start_response(self.status, self.headers)
        return [template.render(**kwargs).encode('utf-8')]

    def reply(self,text):
        self.headers.append(('Content-Type', 'text/html'))
        self.request.start_response(self.status, self.headers)
        return [text.encode('utf-8')]
    def setCookie(self,key, value, expired=None, domain=None, path='/'):
        values = key + "=" + str(value) + ";"
        #id=010;Max-Age=30;domain=localhost;path=/
        if expired:
            values += "Max-Age=" + str(expired) + ";"
        if domain:
            values + "domain=" + str(domain) + ";"
        values += "path=" + str(path)
        self.headers.append(("Set-Cookie", values))

def render(request,file,data):
    response = MyResponse(request)
    return response.load(file,data)


