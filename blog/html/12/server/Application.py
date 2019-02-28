def Application(environ,start_response):
    path_info = environ['PATH_INFO']
    path_info = path_info.strip('/') + '/'
    print(environ["QUERY_STRING"])
    content = ""
    if path_info == 'login/':
        with open('login.html') as fp:
            content = fp.read()


    start_response("200 ok", [("ContentType", 'text/html')])
    return [content.encode('utf-8')]
