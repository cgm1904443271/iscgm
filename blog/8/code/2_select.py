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
sno = input("请输入学生的姓名：")
# 字符串参数两边需要添加单引号
sql = "select sno, sname, ssex from  student where sname like '{}%'".format(sno)
print(sql)
# 返回受影响的行数
try:
    rows = cursor.execute(sql)
    if rows > 0:
        # print(rows)
        # 4.读取结果集
        # data = cursor.fetchone()   # 一条记录
        # data = cursor.fetchmany(5)  # 多条记录，参数是记录个数
        data = cursor.fetchall()  # 获取所有记录
        print(data)
        # print(cursor._executed)  # 获取所执行的sql语句
except Exception as e:
    print(e)
finally:
    # 5.关闭链接
    cursor.close()
    conn.close()

