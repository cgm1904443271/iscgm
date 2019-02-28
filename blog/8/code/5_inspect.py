from hashlib import sha1

import pymysql

# 1.链接数据库                                   )
conn = pymysql.Connect(host='localhost',
                       user='root',
                       password='234',
                       database='student1',
                       port=3306,
                       charset='utf8')

# 2.创建游标
# 如果不指定参数，默认返回的元组: (('001', '刘凯', '男'), ('002', '邹辉', '男'), ('003', '邵壮', '男'), ('004', '温祖斌', '男'), ('005', '张鹏', '男'))
# 如果指定cursor=pymysql.cursors.DictCursor，返回的是列表：[{'sno': '001', 'sname': '刘凯', 'ssex': '男'}, {'sno': '002', 'sname': '邹辉', 'ssex': '男'}, {'sno': '003', 'sname': '邵壮', 'ssex': '男'}, {'sno': '004', 'sname': '温祖斌', 'ssex': '男'}, {'sno': '005', 'sname': '张鹏', 'ssex': '男'}]
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 3.执行sql语句
name = input("请输入用户名：")
password = input("请输入密码：")
password = sha1(password.encode('utf-8')).hexdigest()

# 字符串参数两边需要添加单引号
# 请输入用户名：lll' or '1' or '
# 请输入密码：esrsers
# select id from  user where name = 'lll' or '1' or '' and password='290dd95a726253d2ae4c06aae800fca5be756b72'
# 登陆成功
# 所谓注入式攻击，就是通过构造特殊输入构成永真条件，进入系统获取数据
# sql = "select id from  user where name = '{}' and password='{}'".format(name,password)
# print(sql)
# exit()

# 1.使用escape方法对特殊字符转义
# name = pymysql.escape_string(name)
# sql = "select id from  user where name = '{}' and password='{}'".format(name,password)

# 2使用execute方法本身的转义功能
sql = "select id from  user where name = %s and password=%s"
# print(sql)
# exit()
# 返回受影响的行数
try:
    rows = cursor.execute(sql,(name,password))
    print(cursor._executed)
    if rows > 0:
       print("登陆成功")
    else:
        print("登录失败")
except Exception as e:
    print(e)
finally:
    # 5.关闭链接
    cursor.close()
    conn.close()

