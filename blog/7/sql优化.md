# mysql优化

## 一、数据库设计原则

### 数据库设计的三范式

学生表(学号，姓名，生日，课程名，课程成绩，等级，学院，院长)

| 学号    | 姓名   | 生日       | 课程号         | 课程名        | 成绩    | 等级   | 学院    | 院长   |
| ----- | ---- | :------- | ----------- | ---------- | ----- | ---- | ----- | ---- |
| 10001 | 张三   | 1998.1.1 | tp3021,h333 | 计算机原理，高等数学 | 87，90 | B,A  | 计算机学院 | xxx  |

- 第一范式  表中每一个属性不可再分，不允许出现表中套表的情况

  | 学号    | 姓名   | 生日       | 课程号    | 成绩   | 等级   | 学院    | 院长   |
  | ----- | ---- | -------- | ------ | ---- | ---- | ----- | ---- |
  | 10001 | 张三   | 1998.1.1 | tp3021 | 87   | B    | 计算机学院 | xxx  |
  | 10001 | 张三   | 1998.1.1 | h333   | 90   | A    | 计算机学院 | xxx  |

  | 课程号    | 课程名   |
  | ------ | ----- |
  | tp3201 | 计算机原理 |
  | h333   | 高等数学  |

  ​

- 第二范式  

  ~~~
  键/码   区分不同记录，可以一个属性或者多个属性的组合，主键是指定的键
  每一个非主属性（不保含在任何一个键里的属性）必须完全依赖于主键（不存在非主属性部分依赖于码）
  ~~~

  | 学号   | 姓名   | 生日   | 学院编号 |
  | ---- | ---- | ---- | ---- |
  |      |      |      |      |

  | 学院编号 | 学院   | 院长   |
  | ---- | ---- | ---- |
  |      |      |      |

  | 学号   | 课程号  | 成绩   | 等级   |
  | ---- | ---- | ---- | ---- |
  |      |      |      |      |

  ​

- 第三范式

  ~~~
  第三范式： 不存在非主属性传递依赖于主码

  ~~~

  | 学号   | 课程号  | 成绩   |
  | ---- | ---- | ---- |
  |      |      |      |

  | 等级编号 | up   | down | 等级   |
  | ---- | ---- | ---- | ---- |
  | 1    | 100  | 90   | A    |
  | 2    | 89   | 80   | B    |

  ​

- 反范式设计

  - 如果考虑查询性能，应该尽量减少表的关联
  - 将经常查询的数据都放到一个表里，尽量少采用字典表


### 表设计

- 尽量选用长度小的类型

- 能选用整型，不要选用字符串

- 日期型能用date就不要使用datetime，不准用字符串存储日期

- 字段不要设置默认值null

- 主键一般无意义，用整型，自增

  

## 二、sql语句的优化

1.开启慢查询

~~~
在mysql下查询
mysql> show VARIABLES like '%slow%';
+---------------------------+--------------------------------+
| Variable_name             | Value                          |
+---------------------------+--------------------------------+
| log_slow_admin_statements | OFF                            |
| log_slow_slave_statements | OFF                            |
| slow_launch_time          | 2                              |慢查询的阈值，超过这个值认为是慢查询
| slow_query_log            | OFF                            |慢查询是关闭的
| slow_query_log_file       | /var/lib/mysql/ubuntu-slow.log |慢查询日志文件路径
+---------------------------+--------------------------------+
5 rows in set (0.01 sec)

sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

#在[mysqld]后面增加
long_query_time = 1   #超过1秒钟的sql记录下来
log-slow-queries = /var/mysql/log/log.txt  #慢查询的日志文件
log-queries-no-using-indexes   #把没使用索引的查询记录下来
~~~

2 使用explain/desc分析sql语句

~~~
explain  select ...    #分析sql语句，sql语句本身并不执行
explain select name ,age from user where age >10
    -> ;
+----+-------------+-------+-------+---------------+-----------+---------+------+------+-------------+
| id | select_type | table | type  | possible_keys | key       | key_len | ref  | rows | Extra       |
+----+-------------+-------+-------+---------------+-----------+---------+------+------+-------------+
|  1 | SIMPLE      | user  | range | index_age     | index_age | 2       | NULL |    2 | Using where |
+----+-------------+-------+-------+---------------+-----------+---------+------+------+-------------+
1 row in set (0.00 sec)
select_type  :  查询的类型  
              simple 指单表查询（不使用连接、子查询）
              primary： 主查询
              union  联合查询的第二个sql语句，或后面的查询
              subquery  子查询
table   表名
type    查询方式：
	all
		全表扫描，对于数据表从头到尾找一遍
		如果有limit限制，则找到之后就不在继续向下扫描
			select * from tb1 where email = 'seven@live.com'
			select * from tb1 where email = 'seven@live.com' limit 1;
				找到一个后就不再继续扫描
	index
		全索引扫描，对索引从头到尾找一遍
			select id from student;
	range
		对索引列进行范围查找
	index_merge
		合并索引，使用多个单列索引搜索
	ref_or_null
	ref
		根据索引查找一个或多个值
	eq_ref
		连接时使用primary key 或 unique类型
	const
		常量
		表最多有一个匹配行,因为仅有一行,在这行的列值可被优化器剩余部分认为是常数,const表很快,
		因为它们只读取一次
	system
		系统，表仅有一行(=系统表)。这是const联接类型的一个特例
	性能
		all < index < range < index_merge < ref_or_null < ref < eq_ref < system/const
 possible_keys  可能被用到的索引
 key             使用的索引
 key_len         索引字段最大使用长度
 rows            影响的行数，越小越好
 
 关注：type 、key、rows
 
~~~

3 优化sql语句

~~~
1 查询的时候不要使用select *
2.尽量使用limit 1 取得唯一的一行
3.尽量使用索引字段进行查询
4 可以使用覆盖索引加速查询  （一个索引包含了查询结果中所有的字段）
5 尽量少用like 或者or
6 不要使用全文索引，如果非要使用可以把全文索引独立出来，建立全文索引服务器
7 关联查询的时候，关联的字段都应该有索引
8 不要使用!=操作，不使用索引
9 查询的时候类型不匹配不使用索引
10 联合索引不带左前缀，不使用索引
11 尽量减少子查询，可以使用关联查询代替子查询
    select count(*) from article where uid in(select uid from user where id=10)
    select count(*) from aticle,user where user.id = aticle.uid   and user.id=10
    select count(*) from aticle join user on user.id=article.uid  where userid.id=10
12 尽量多试验不同sql语句，比较他们的效率，采用最少
13 不要在where中，运算符左边运算,只要是计算，不采用索引
    select username from user where age/2>10
14 不要在where中，运算符左边不要出现任何函数,否则不采用索引
   select COUNT(*) from user where year(birthday) == 1993;
15 不要对null判断 ，否则不使用索引
16 避免默认排序
    select cid,count(*) from bbs group by cid
    select cid,count(*) from bbs group by cid order by null #不排序
~~~

4 其他优化措施

~~~
在应用层面可以nosql技术，把数据保存redius、memcached中加速查询
从架构方面：读写分离
可以使用mysql分区技术，把一个表分为多个文件
分库分表分机器
把表进行垂直切分，或水平切分

~~~

数据库设计 ====》索引 ===》SQL语句优化 ===》分区=》nosql缓存 ==》读写分离=》分库分表分机器（数据库中间件）=》表的垂直/水平切分



## 其他技术

### 1. 存储过程

### 2. 触发器

### 3. 数据分区

### 4. 读写分离

### 5. 主从复制