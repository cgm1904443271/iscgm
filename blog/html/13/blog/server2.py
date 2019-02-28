# 创建自己的测试web服务器
from wsgiref.simple_server import make_server
from application import application
# 第一个参数是服务器地址
# 第二个参数是端口
# 第三个参数是我们自己的应用
server = make_server('',9090,application)
print("服务器已启动，端口：9090")
server.serve_forever()
