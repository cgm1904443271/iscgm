# pymysql操作mysql数据库

## 一、pymysql操作mysql数据库

- 安装pymysql

  ```
  pip install pymysql
  ```

### 1.1 pymysql操作数据库的五行拳

1. 连接数据库

   使用Connect方法连接数据库

   ```
   pymysql.Connections.Connection(host=None, user=None, password='', database=None, port=0,  charset='')
   参数说明：
       host – 数据库服务器所在的主机。
       user – 登录用户名。
       password – 登录用户密码。
       database – 连接的数据库。
       port – 数据库开放的端口。（默认: 3306）
       charset – 连接字符集。
   返回值：
      返回连接对象
      
   例子：
   link = pymysql.Connect(host='localhost', port=3306, user='root', password='123456', db='zzl', charset='utf8')
   
   ```

   - 连接对象方法

   | 方法                 | 说明                        |
   | -------------------- | --------------------------- |
   | begin()              | 开启事务                    |
   | commit()             | 提交事务                    |
   | cursor(cursor=None)  | 创建一个游标用来执行sql语句 |
   | rollback()           | 回滚事务                    |
   | close()              | 关闭连接                    |
   | select_db(db)        | 选择数据库                  |
   | set_charset(charset) | 设置字符集                  |

2. 创建游标

   ```
   cursor = link.cursor()  
      cursor=pymysql.Cursors.DictCursor()  #[{}]
   print(cursor.rowcount) #打印受影响行数
   ```

   | 方法                      | 说明                                                         |
   | ------------------------- | ------------------------------------------------------------ |
   | close()                   | 关闭游标                                                     |
   | execute(query, args=None) | 执行单条语句，传入需要执行的语句，是string类型；同时可以给查询传入参数，参数可以是tuple、list或dict。执行完成后，会返回执行语句的影响行数。 |
   | fetchone()                | 取一条数据                                                   |
   | fetchmany(n)              | 取多条数据                                                   |
   | fetchall()                | 取所有数据                                                   |
   | _executed属性             | 正在执行的sql语句                                            |

3. 执行sql语句

   ```
   # 执行sql语句
   sql = 'select * from user1'
   # 执行完sql语句，返回受影响的行数
   num = cursor.execute(sql)
   ```

4. 获取结果集

   ```
   result1 = cursor.fetchone()
   print(result1)
   ```

5. 关闭连接

   ```
   cursor.close()
   link.close()
   ```

- 注意：

  写完代码后，需要将py文件添加可执行权限 

  ```
  sudo chmod +x conndb.py
  ./conndb.py
  ```

  ​

### 1.2 pymysql中事务处理

pymysql默认是没有开启自动提交事务，所以我们如果进行增、删、改，就必须手动提交或回滚事务。

```
sql = 'delete from user where id=%s' % user_id

# 如果要执行增删改语句的时候，下面的就是固定格式
try:
	cursor.execute(sql)
	# 如果全部执行成功，提交事务
	link.commit()
	print(cursor.lastrowid) #获取最后插入记录的自增id号
except Exception as e:
	print(e)
	link.rollback()

```

### 1.3 防sql注入

- pymysql.escape_string(str)  转移字符串中特殊字符（‘，“等）
- cursor.execute(sql,参数)，参数化，不要直接拼接sql字符串

## 二、封装数据库操作类

### 2.1.数据库操作类的封装

- 一个数据库model类对应一个表

- 数据库model类的核心是连贯操作和方法的无顺序调用

  ~~~
  db.where('username="admin"').table('blog_user').field('username,password').select()
  # select usenrame,password from blog_user where username='admin'
  # sql = "SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}".format()
  ~~~

### 2.2 连贯操作

  方法要返回self

### 2.3 方法的无顺序调用

- 在进行数据库查询时，不用考虑方法的先后顺序。
- 核心思想
  - 无论怎么调用，最终生成sql语句。
  - 每调用一个方法，就生成对应sql子句
  - 涉及到的技术点：字符串拼接
  -  每次调用的最后必定是select、insert、update、delete，这些方法不返回self

### 2.4 字段缓存

- 在查询语句中尽量不要出现*，我们可以将表的字段缓存的文件中，实例化数据库model类时，加载缓存字段，如果不指定字段就使用缓存字段
- 也可以通过缓存字段过滤增删改时无效的字段

## 三、分页类

分页是通过解析url中page参数（可以自己指定），结合sql语句中limit子句，从数据库中查询每个页面所需数据，具体可以分为以下步骤：

- 1） 获取总记录数
- 2）获取每页显示的记录个数
- 3）计算总页数：总记录数/每页记录个数，然后上取整
- 4）解析url获取当前页数
- 5）计算limit子句所需的偏移量： limit (当前页数-1)*每页记录个数，每页记录个数