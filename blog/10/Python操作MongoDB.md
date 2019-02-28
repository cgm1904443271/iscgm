# Python操作MongoDB

## 一  安装 pymongo

~~~
pip  install  pymongo==3.4

导入 MongoClient
from pymongo import MongoClient
~~~



## 二 连接MongoDB数据库

~~~
MongoDB端口号:27017
连接MongoDB我们需要使用PyMongo库里面的MongoClient，一般来说传入MongoDB的IP及端口即可，第一个参数为地址host，第二个参数为端口port，端口如果不传默认是27017。
conn= MongoClient("localhost")
~~~

## 三 选择数据库

~~~
连接数据库
    db = conn.数据库名
连接集合
	collection = db['表名']
	or
	collection = db.表名
查看表
    db.collection_names()
~~~

## 四 INSERT 数据的插入

#### (1) 插入一条数据

   	db.collection.insert({'name':'大坏蛋','age':23})

  	插入成功：返回ID

#### (2) 插入多条

​	db.collection.insert([{'name':'大坏蛋','age':23},{'name':'猪队友','age':30}])

​	插入成功：返回ID的列表

​        [ObjectId('5a1642c4b96166349c2963eb'), ObjectId('5a1642c4b96166349c2963ec')]

#### (3) 3.2以上的插入函数

​	db.collection.insert_one()  		插入一条数据

​	db.collection.insert_many()	插入多条数据，插入成功:返回obj

#### (4) 3.2以上获取插入的id

​	db.collection.insert_one()返回的就是id

​	res = db.collection.insert_many()  #返回的是对象

​          可以通过res.inserted_ids获取插入多条的ID

## 五 find 查询

#### (1) find 查询

~~~
res = db.user.find()  #返回的是游标对象 使用next() 方法 进行取值
print(res.next());
print(list(res));  #显示全部

#遍历
for obj in res:
    print(obj)
~~~

#### (2) 查询一条

```python
res = db.user.find_one(条件) #返回一条记录
```

#### (3) 条件查询

~~~
res = db.user.find({"name":"张三"})
for obj in res:
    print(obj)
~~~

#### (4)id查询

~~~
from bson.objectid import ObjectId* #用于ID查询
data = db.user.find({"_id":ObjectId("59a2d304b961661b209f8da1")})
~~~

#### (5)模糊查询

​    MongoDB查询条件可以使用正则表达式，从而实现模糊查询的功能。模糊查询可以使用$regex操作符或直接使  用正则表达式对象。

1. ##### $regex

2. ##### re.compile()

   import re  使用 re.compile()

   | MySQL                                    | MongoDB                                  |
   | ---------------------------------------- | ---------------------------------------- |
   | select * from student where name like ’%joe%’ | db.student.find({name:{"$regex":"坏"}})   |
   | select * from student where name regexp ’joe’ | db.student.find({"name":re.compile("坏")) |

   ~~~
   import re
   data = db.user.find({"name":{"$regex":"五"}})
   data = db.user.find({"name":re.compile("五")})
   ~~~

注意 当匹配类型为 不是字符串的类型的时候 匹配不出来
    data = db.user.find({"age":re.compile("30")})
    data = db.user.find({"age":{"$regex":"3"}})
    ret = collection.find({'name':re.compile(r'^郭')})



#### (6) sort 排序

~~~
#sort 排序
data = db.user.find().sort("age",1)  #按照年龄升序
data = db.user.find().sort("age",-1)  #按照年龄降序
for i in data:
     print(i)

~~~

#### (7) limit 取值

   ~~~
#limit 取值
print(next(db.user.find().sort("age",-1).limit(1)))  #取出年龄最大的一条数据
   ~~~

#### (8) skip 跳过

~~~
#skip   跳过最大值 取第二大值
print(next(db.user.find().sort("age",-1).skip(1).limit(1)))  #取出年龄最大的一条数据
~~~



## 六 update 修改

##### (1) db.collection.update(条件,更改)

```python
data = db.user.update({"name":"潘金莲"},{"$inc":{"age":2}})  #累加修改
data = db.user.update({"name":"潘金莲"},{"$set":{"age":2}})  #直接修改

更改成功 返回 数据:{'n': 1, 'nModified': 1, 'ok': 1.0, 'updatedExisting': True}
```

##### (2) update_one()    修改一条数据

```python
data = db.user.update_one({"name":"王五"},{"$set":{"age":20}})
```

##### (3) update_many()  修改多条数据

```python
data = db.user.update_one({"name":"王五"},{"$set":{"age":20}})  #修改多条
```

##### (4) update_one  和 update_many  返回匹配条数和修改的条数

    result.matched_count 		返回匹配条数
    result.modified_count	    返回修改的条数


## 七 remove 删除

##### (1) remove  匹配到的全部删除

​	db.collection.remove({条件})

##### (2) 删除全部数据

​	db.collection.remove()

##### (3) 依然存在两个新的推荐方法

	delete_one()和delete_many()方法，示例如下：
	
	delete_one()即删除第一条符合条件的数据
	collection.delete_one({“name”:“ Kevin”})
	
	delete_many()即删除所有符合条件的数据，返回结果是DeleteResult类型
	result = collection.delete_many({“age”: {'$lt':25}})
	
	可以调用deleted_count属性获取删除的数据条数。
	result.deleted_count


## 八  关闭数据库链接

conn.close()