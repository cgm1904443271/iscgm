# 定义各种处理
from urllib.parse import parse_qs
from hashlib import sha1
from Manager import Manager
from MyResponse import render,MyResponse

import jinja2

# 首页
# def index(environ,start_response):
#     start_response('200 ok', [('Content-Type', 'text/html')])
#     return [b"<!doctype html><head><meta charset='utf-8'></head><body><h1>Hello world</h1></body></html>"]
def index(request):
    # request.start_response('200 ok', [('Content-Type', 'text/html')])
    # return [b"<!doctype html><head><meta charset='utf-8'></head><body><h1>Hello world</h1></body></html>"]
    response = MyResponse(request)
    cookie = request.cookies
    print(cookie,'id' in cookie)
    # 已登录
    if 'id' in cookie:
        print(111)
        return  response.load('index.html',id=request.cookies.get('id'),username=request.cookies.get('name'))
    else:
        print(222)
        return response.load('index.html')


# 登录
# def login(environ,start_reponse):
#     try:
#         with open('templates/login.html') as fp:
#             data = fp.read()
#         start_reponse('200 ok', [('Content-Type', 'text/html')])
#         return [data.encode('utf-8')]
#     except Exception as e:
#         data = "File Not Found"
#         start_reponse('404 Not Found', [('Content-Type', 'text/html')])
#         return [data.encode('utf-8')]
def login(request):
    print(request.cookies)
    # print(request.environ)
    try:
        with open('templates/login.html') as fp:
            data = fp.read()
        request.start_response('200 ok', [('Content-Type', 'text/html')])
        return [data.encode('utf-8')]
    except Exception as e:
        data = "File Not Found"
        request.start_response('404 Not Found', [('Content-Type', 'text/html')])
        return [data.encode('utf-8')]


# 登录处理
# def doLogin(environ,start_response):
#     print(environ.get("QUERY_STRING"))
#     # 把参数字符串转化为字典
#     paras = parse_qs(environ.get('QUERY_STRING',''))
#     username = paras.get('username')
#     if username:
#         username = username[0]
#     password = paras.get('password')
#     if password:
#         password = password[0]
#         # 加密
#         password = sha1(password.encode('utf8')).hexdigest()
#     # print(username,password)
#
#     # 数据库操作
#     db = Manager('user')
#     result = db.where(name=username,password=password).select()
#     start_response('200 ok', [('Content-Type', 'text/html')])
#
#     # 如果查询成功
#     if result:
#         html=""
#         with open('templates/tip.html') as fp:
#             html = fp.read()
#         return [html.encode('utf-8')]
#     else:
#         return ["用户名或密码错误，请重新登陆".encode('utf-8')]

def doLogin(request):
    # 把参数字符串转化为字典
    paras = request.GET
    # print(paras)
    username = paras.get('username')
    password = paras.get('password')
    password = sha1(password.encode('utf8')).hexdigest()
    # print(username,password)

    # 数据库操作
    db = Manager('user')
    result = db.where(name=username,password=password).select()
    # request.start_response('200 ok', [('Content-Type', 'text/html')])

    # 如果查询成功
    if result:
        response = MyResponse(request)
        print(result)
        response.setCookie('name',result[0]['name'])
        response.setCookie('id',result[0]['id'])
        # html=""
        # with open('templates/tip.html') as fp:
        #     html = fp.read()

        return response.load('index.html')
    else:
        request.start_response('200 ok', [('Content-Type', 'text/html')])
        return ["用户名或密码错误，请重新登陆".encode('utf-8')]

# 退出登录
def logout(request):
    response = MyResponse(request)
    response.setCookie('id','',expired=-1)
    response.setCookie('name','',expired=-1)
    return  response.load('index.html')

# 学生列表
# def studentList(request):
#     html = """"
#     <!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <title>学生列表</title>
#     </head>
#     <body>
#     <table border="1" width="80%" align="center" cellspacing="0">
#         <caption>学生列表</caption>
#         <tr>
#             <th>学号</th>
#             <th>姓名</th>
#             <th>性別</th>
#             <th>生日</th>
#             <th>班級</th>
#         </tr>
#        {}
#     </table>
#     </body>
#     </html>
#     """
#     db = Manager('student')
#     data = db.values('sno,sname,ssex,sbirthday,sclass').select()
#     print(data)
#     from datetime import datetime
#     content = ""
#     for student in data:
#         content += "<tr><td>" + student.get('sno',' ') + "</td>"
#         content += "<td>" + student.get('sname',' ') + "</td>"
#         content += "<td>" + student.get('ssex',' ') + "</td>"
#         content += "<td>" + student.get('sbirthday',' ').strftime("%Y-%m-%d")  + "</td>"
#         if student.get('sclass',' '):
#             content += "<td>" + student.get('sclass',' ') + "</td></tr>"
#         else:
#             content += "<td>" + " " + "</td></tr>"
#
#     html = html.format(content)
#     # print(html)
#     request.start_response('200 ok', [('Content-Type', 'text/html')])
#     return [html.encode('utf-8')]

def studentList(request):
    db = Manager('student')
    data = db.values('sno,sname,ssex,sbirthday,sclass').select()
    print(data)
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
    template = env.get_template('studentlist.html')
    print(template)
    request.start_response('200 ok', [('Content-Type', 'text/html')])
    return [template.render(students=data).encode('utf-8')]

# 学生信息
def studentInfo(request,sno):
    print(sno)
    request.start_response('200 ok', [('Content-Type', 'text/html')])
    return [b'info']

def register(request):
    print('register')
    html = b''
    with open('templates/register.html' ,'rb') as fp:
        html = fp.read()
    request.start_response('200 ok', [('Content-Type', 'text/html')])
    return [html]

def loadStatic(request):
    path = request.path.strip('/')
    # print(path)

    import os
    ext = os.path.splitext(path)[1].strip('.')
    print(ext)
    if os.path.exists(path):
        with open(path,'rb') as fp:
            content = fp.read()
        if ext == 'css':
            request.start_response('200 ok', [('Content-Type', 'text/css')])
        elif ext == 'js':
            request.start_response('200 ok', [('Content-Type', 'application/x-javascript')])
        elif ext == 'png':
            request.start_response('200 ok', [('Content-Type', 'image/png')])
        elif ext in ['jpeg','jpg']:
            request.start_response('200 ok', [('Content-Type', 'image/jpeg')])

    else:
        content = b"file not found"
        request.start_response('200 ok', [('Content-Type', 'text/html')])
    return [content]

def yzm(request):
    from VerifyCode import VerifyCode
    vc = VerifyCode()
    data = vc.generate()
    print(vc.code)
    request.start_response('200 ok', [('Content-Type', 'image/png')])
    return [data]

def test(request):
    print("111")
    # print(request.cookies)
    response = MyResponse(request)
    response.setCookie('name','tom',1000)
    print("222")
    return response.reply("哈哈哈")

def area(request):
    response = MyResponse(request)
    return response.load('area.html')

def province(request,aid):
    print(aid)
    db = Manager('areainfo')
    res = db.where(pid=aid).select()
    print(res)
    import json
    data = "数据不存在"
    if res:
        data = json.dumps(res)

    request.start_response('200 ok', [('Content-Type', 'application/json')])
    return [data.encode('utf-8')]
def hello(request):
    response= MyResponse(request)
    return response.load('hello.html')
def jsonp(request,aid,funcname):
    print(aid,funcname)
    db = Manager('areainfo')
    res = db.where(pid=aid).select()
    print(res)
    import json
    data = "数据不存在"
    if res:
        data = json.dumps(res)
    s1 = funcname + "(" + data+")"
    request.start_response('200 ok', [('Content-Type', 'text/html')])
    return [s1.encode('utf-8')]

def ajax(request):
    print(111)
    response = MyResponse(request)
    return response.load('ajax.html')
def get(request):
    # print(request.GET)
    print(request.POST)
    import json
    data = [{'id':2,'name':'test01','password':'23874872edd'}]
    data = json.dumps(data)
    request.start_response('200 ok', [('Content-Type', 'application/json')])
    return [data.encode('utf-8')]