import  redis

# 链接redis
r = redis.StrictRedis(host='127.0.0.1',port=6379,password='123')

# 设置键值对
# r.set('fangjia','下午考完试你就解放了')
# # 返回值是字节流字符串
# data = r.get('fangjia')
# print(data.decode('utf8'))

# 方式2
pipe = r.pipeline()
pipe.set('aa',100)
pipe.set('bb',20)
pipe.execute()

print(r.get('aa'))