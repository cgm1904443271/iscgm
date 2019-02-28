import redis
from hashlib import sha1
from Manager import Manager

name = input("请输入用户名")
password = input("请输入密码")
password = sha1(password.encode('utf8')).hexdigest()

# 链接redis
r = redis.StrictRedis(host='localhost',password='123')

# 1.到redis中获取数据
# 假定用户名不允许重复
if r.exists("user:"+name):  # redis中存在
    print("数据在reids")
    passwd = r.hget("user:"+name,'password').decode('utf8')
    print(passwd)
    if password == passwd:
        print("登陆成功")
    else:
        print("登陆失败")
else:
    # 到mysql中查询
    db = Manager('user')
    data = db.where(name=name,password=password).values('id').select()
    if data:
        # 缓存到redis
        r.hset("user:"+name,'name',name)
        r.hset("user:"+name,'password',password)

        print("在mysql")
        print("登陆成功")
    else:
        print("用户或密码错误")


