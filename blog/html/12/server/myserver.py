from wsgiref.simple_server import  make_server
from Application import Application

server = make_server('',8081,Application)

server.serve_forever()