from pymongo import MongoClient

# 链接mongo
conn = MongoClient(host='localhost')


# 链接数据库
db = conn.student

# 查询
# 返回一个可迭代对象
# data = db.student.find()
# data = db.student.find({'age':{'$lt':50}})
# print(data)
# for value in data:
#     print(value)

# data = db.student.find().sort('age',-1)
# print(list(data)) #转列表


# insert
# db.student.insert({'name':'tom','age':20})

# update
# db.student.update({'name':'tom'},{'$set':{'name':'林青霞'}})

# delete
db.student.delete_many({'age':20})

data = db.student.find()
print(list(data)) #转列表

conn.close()
