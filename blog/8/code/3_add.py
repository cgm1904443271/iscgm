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
info = input("请输入学生的信息（学号/姓名/班级,用逗号隔开）：")
sno, sname, sclass  = info.split(',')  # 列表的解包
sql = "insert into student(sno,sname,sclass) values('{}','{}','{}')".format(sno,sname,sclass)
# print(sql)
# exit()
# 返回受影响的行数
try:
    # pymysql自动开启事务，关闭了自动提交功能
    rows = cursor.execute(sql)
    if rows > 0:  # 插入成功
        conn.commit()   # 提交
    else:
        conn.rollback()  # 回滚

except Exception as e:
    print(e)
finally:
    # 5.关闭链接
    cursor.close()
    conn.close()

