# MongoDB 数据库

## 一、MongoDB 概念解析

- 什么是MongoDB？
  ​    1、MongoDB是有C++语言编写的，是一个基于分布式文件存储的开源数据库系统，在高负载的情况下，添加更多节点，可以保证服务器的性能
  ​    2、MongoDB为web应用提供了高性能的数据存储解决方案
  ​    3、MongoDB将数据存储为一个文档，数据结构由(key->value)形式组层，MongoDB文档类似于json文件，字段值可以是其他文档，列表等

- JSON文件

  存储数据的一种格式


      {}：代表字典
      []：列表
      ,：分隔两个部分
      :：键值对
      {
          "code": 1,
          "totle": 3,
          "pers": [
              {
                  "name":"tom1",
                  "age":18
              },
              {
                  "name":"tom2",
                  "age":19            
              },
              {
                  "name":"tom3",
                  "age":17            
              }
          ]
      }

- 特点

  1、MongoDB提供了一个面向文档存储，基本思路是将原来的“行”的概念换成了更加领过的“文档”模型，一条记录可以表示非常复杂的层次关系
  2、MongoDB支持丰富的查询表达式，查询指令是json形式的标记，可以轻易查询文档中嵌套的对象和列表
  3、非常容易扩展，扩展集群后还可以实现集群中的数据的负载均衡。
  4、MongoDB支持各种编程语言，比如python、Java、c++、c、php、c#、ruby、JavaScript等
  5、丰富的功能，包括索引、存储JavaScript、聚合、固定集合、文件存储等功能
  6、方便管理，处理启动数据库服务以外，记过没有其他什么必要的操作。管理集群只需要知道有哪个新增的节点即可，自动继承和配置新节点


|  SQL术语/概念   | MongoDB术语/概念 |           解释/说明           |
| :---------: | :----------: | :-----------------------: |
|  database   |   database   |            数据库            |
|    table    |  collection  |           表/集合            |
|     row     |   document   |           行/文档            |
|   column    |    field     |          数据字段/域           |
|    index    |    index     |            索引             |
| table joins |              |      表关联/MongoDB不支持       |
| primary key | primary key  | 主键索引/mongodb自动将_id设置为主键索引 |

## 二、  MongoDB创建数据库

### (1) 安装mongoDB

~~~shell
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

#下面命令针对ubuntu16.04版本，在其他ubuntu版本系统请查看MongoDB官网
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list
sudo apt-get update
sudo apt-get install -y mongodb-org

查看服务是否启动
pgrep mongo -l

#查看版本
mongo -version

手动启动
mongod
或者
sudo service mongod start | stop | restart
~~~

### (2) 进入 MongoDB数据库

~~~
> mongo
~~~



## 三、 对于库的操作 database

一个MongoDB服务器中可以建立多个数据库，系统保留数据库包括：

- admin
   从权限的角度考虑，这是“root”数据库，要是将一个用户添加到这个数据库，这个用户自动继承所有数据库的权限，一些特定的数据库服务端的命令只有能从这个数据库运行，比如列出所有的数据库或者关闭服务
- local
   这个数据库永远不会被复制，用来存储仅限于本地单台服务器的一些集合
- config
  当MongoDB用于分片设置时，config数据库在内部使用，用于保存分片的相关数据

数据库命名规范：

- 不能是空字符串（"")
- 不得含有' '（空格)、.、$、/、\和\0 (空字符)
- 应全部小写

### (1) 创建库 

use 库名

注意：

1. 当use一个不存在的库的时候  其实这个库已经创建出来了 但是里面没有数据 使用show dbs的时候 ，该库不会显示
2. mongodb严格区分大小写
3. 数据库名字不要用admin、local和config

在MongoDB里 不管是什么操作 都是db。

```python
语法：db.getName()  获取当前的所在的库
语法：db      获取当前所属的库
```

### (2) 删除数据库

- 删除数据库之前最好use一下  确定自己所在哪个库下

     ~~~
     语法：db.dropDatabase()
     ~~~

### (3) 查看所有的库

~~~
语法：show dbs
~~~

## 四、 对于集合的操作 collection

集合相当于关系型数据库中的表，但集合中的数据不必是同一种类型，可以是不同种类型。

- 集合的名称不能以system.开头
- 名称不能是保留字
- 名称不能是空字符

### (1) 创建集合（也就是创建表）

~~~
语法：db.createCollection('集合名称')
示例：db.createCollection('user')  #在当前的库里面创建一个空user集合

语法：db.集合名称.insert(文档)
示例：db.student.insert({name:'tom',age:20}) #创建一个student集合并插入了一个文档
~~~

### (2) 删除集合

~~~
语法：db.集合名.drop()
示例：db.user.drop()  #删除user集合
~~~

### (3) 显示所有集合

~~~
语法：show collections
~~~

## 五、 文档操作

文档是MongoDB中最核心的概念，是其核心单元，将文档类比成关系型数据库中的每一行数据
多个键及其关联的值有序的放在一起就是文档，MongoDB使用了Bson数据结构来存储数据和网络数据交换
BSON数据可以理解为在JSON的基础上添加了一些json没有的数据类型

MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成。MongoDB 文档类似于 JSON 对象。字段值可以包含其他文档，数组及文档数组。

![document](document.png)

注意：

- 文档的键/值对是有顺序的
- 文档的键不能重复，如果重复，后面的会覆盖前面的键
- MongoDB区分大小写和类型
- 文档中的键一般是字符串

文档命名规范

- 文档的键区分大小写
- 文档的键不要使用\0和$

### 5.1 插入文档

#### (1) insert的插入一条文档

~~~
语法：db.集合名.insert(文档)
示例：db.user.insert({name:'tom',age:20})
~~~

#### (2) insert 插入多条文档

~~~
语法：db.集合名.insert([文档1,文档2,...文档2])
示例：db.user.insert([{name:'武大郎',age:30},{name:'和珅',age:20}])
~~~

- **注意：**如果没有中括号 那么只会将第一条数据 插入成功

#### (3) save 

~~~
语法：db.集合名.save(文档)
说明：如果不指定_id字段，save()方法类似于insert()方法。如果指定_id字段，则会更新_id字段的数据
示例1：db.student.save({name:"科比", age:22,address:"洛杉矶"})
示例2：db.student.save({_id:ObjectId("59950962019723fe2a0d8d17"),name:"姚明", age:23,address:"休斯顿"})
~~~

#### (4)3.2版本以后 建议使用

~~~
语法：db.collection.insertOne()
示例：db.user.insertOne({name:'萧峰',age:30})

语法：db.collection.insertMany()
示例：db.user.insertMany([{name:'武大郎',age:30},{name:'和珅',age:20}])
~~~

### 5.2 REMOVE文档删除 

~~~
语法： 
db.collection.remove(
   <query>,
   <justOne>
)
参数说明：
      query：可选，删除的文档的条件
      justOne：可选，如果为true或1，则只删除一个文档
示例：
  db.user.remove({name:'武大郎'},1) #会删除第一个匹配到的文档
  db.user.remove({name:"张三"})      #删除多条文档
  db.collection.remove({})    #删除当前集合的全部文档
~~~

- 3.2版本以后 建议使用
  - db.collection.deleteOne()   #删除一条文档
  - db.collection.deleteMany() #删除多条文档


### 5.3 update 修改

```
语法：db.collection.update(条件,修改的操作,{upsert:bool,multi:bool})   
说明：upsert：可选，如果不存在修改的记录，是否当新数据插入，true为插入，False为不插入，默认为false
      multi：可选，默认是false，只更新找到的第一条记录；如果为true,就按照条件查找出来的数据全部更新 
示例：
 $set   直接修改
 $inc   累加修改
db.user.update({name:"潘金莲"},{$set:{age:20}})   #把name为潘金莲的文档的age直接改为20  
db.user.update({name:"潘金莲"},{$inc:{age:20}}) #把name为潘金莲的文档的age加上20 
全部修改：db.user.update({name:"王五"},{$inc:{age:3}},{multi:true})
```

- 3.2版本以后 建议
  updateOne()	只更新一条
  updateMany()	更新多条

### 5.4 FIND 查询

#### (1) 基本查询

~~~
语法：db.collection.find()	查询所有
语法：db.collection.find({条件},{key:1 [,key2:1]})  按照条件来查询  设置为1则显示
语法：db.collection.find({条件},{key1:0[,key2:0]})  按照条件来查询  设置为0则不显示

示例：db.user.find({name:"王五"},{name:1})	#查询所有name为王五的文档 只显示name的值
示例：db.user.find({name:"王五"},{name:0})	#查询所有name为王五的文档 显示name键值对以外的所有的值
示例：db.user.find({},{key:1})		#条件是 查询所有 只显示某个键值对
~~~

- 注意：

```python
错误写法:db.user.find({name:"王五"},{age:1,name:0}) 要么指定显示，要么指定不显示，不可以混合
正确写法：db.user.find({name:"王五"},{_id:0,name:1}) #id隐藏，只显示name的键值对，除了设置系统的_id 可以混搭外 其它都不可以
```

#### (2) findOne 查询一条数据

~~~
语法：db.collection.findOne({条件},{key1:1[key:1]})
示例：db.user.findOne({name:'和珅'},{name:1})
~~~

#### (3) pretty 展开显示

​    db.collection.find().pretty()  #只有当文档一行显示不下(比较长的时候) 会展开显示

#### (4) 统计count	

~~~
db.collection.find().count()  统计所有文档的条数
db.user.find({name:"王五"}).count() 统计满足条件的文档的条数
~~~

#### (5) 条件运算

|     操作符     |      说明       |                             使用                             |
| :------------: | :-------------: | :----------------------------------------------------------: |
|      $gt       |      大于       |         db.user.find({age:{$gt:30}},{age:1})年龄>30          |
|      $gte      |    大于等于     |        db.user.find({age:{$gte:30}},{age:1})年龄>=30         |
|      $lt       |      小于       |         db.user.find({age:{$lt:30}},{age:1})年龄<30          |
|      $lte      |    小于等于     |        db.user.find({age:{$lte:30}},{age:1})年龄<=30         |
|     键:值      |      等于       |                    db.user.find({age:30})                    |
|                |    >= and <=    |          db.user.find({age:{`$gte:25`,`$lte:35`}})           |
| _id:objectId() |    id来查询     | db.user.find({"_id" : ObjectId("5a162218fa08a5e7ad2ad09c")}) |
|     /数据/     |    模糊查询     |            db.user.find({name:/李/}) 名字包含李的            |
|    /^数据/     | 以数据作为开头  |                  db.user.find({name:/^李/})                  |
|    /数据$/     | 以数据作为结尾  |                  db.user.find({name:/五$/})                  |
|      $in       |  在...范围之内  |              db.user.find({age:{$in:[23,30]}})               |
|      $nin      | 不在...范围之内 |         db.user.find({name:{$nin:['王五','赵六']}})          |
|      $ne       |     不等于      |              db.user.find({name:{$ne:'王五'}})               |

#### (6)逻辑运算

~~~
1.and   逻辑与查询
语法：db.集合名.find({条件1,条件2,……,条件n})
示例：db.user.find({name:'赵六',age:54}) 	查询 name为赵六 并且 age为54的文档
      db.user.find({name:"赵六",age:{$gt:40}})	查询name为赵六 并且年龄大于40
2.or 逻辑或
语法：db.集合名.find({$or:[{条件1},{条件2},……,{条件n}]})
示例：db.user.find({$or:[{name:"王五"},{age:40}]}) 	查询name为王五 或者age为40的文档
     db.user.find({$or:[{name:"王五"},{name:"赵六"}]})		查询name为王五或者赵六的所有文档
3. and和or联合使用
语法： db.collection.find( { 条件1,条件2，... $or:[ {条件1} , {条件2}]  })
示例：db.user.find({name:"王五",$or:[{age:30},{age:40}]})查询name为 王五 年龄为30或者40的所有文档
db.user.find({name:'习大大',$or:[{age:66},{age:68}]})
#name='习大大' and (age = 66 or age =68)
~~~

#### (7) limit 和skip

~~~
limit用法：
语法：db.collection.find().limit(num)  #取前num条数据
示例：db.user.find().limit(3)   #取三条数据

skip用法
语法：db.collection.skip(num)   #跳过num条文档
示例：db.user.find().skip(9)  #跳过9条数据

skip 和 limit 配合使用  是分页技术的基础
语法：db.collection.find().skip(num).limit(num)
示例：db.user.find().skip(8).limit(1)   #跳过8条数据 取1条， 其实就是实现了limit m,n
~~~

#### (8) 排序sort   

~~~
语法：db.collection.find().sort(key:1/-1)  #按照key的升序(1)/降序(-1)  
示例：db.user.find().sort({age:-1})   按照年龄 降序显示
     db.user.find().sort({age:-1}).limit(1)  #取出一条年龄最大的文档
~~~


## 六、 数据库的备份

#### (1) 备份

~~~
语法：mongodump -h 主机 -u 用户名 -p 密码 -d 数据库 -c 集合 -o 备份目录
示例：
   mongodump -d bbs -o ./  备份bbs库到当前目录，会生成一个和库名相同的目录
   mongodump -o ./  备份所有数据库
导出集合为json文件：
   mongoexport -d bbs -c user -o ./user.json
~~~

#### (2) 恢复

~~~
语法：mongorestore --drop -d dir/ 恢复所有库   --drop是当恢复时先把之前的数据删除，不建议使用
语法：mongorestore -d mydbdir/   mydbdir就是你数据库备份的目录
语法：mongorestore -d mydb -c test dir/mydb/test.bson  恢复集合
~~~


