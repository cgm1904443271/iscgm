# def test(a=1,b=2,c=3):
#     print(a,b,c)
#
# test()
# test(a=3)
# test(**{'a':1,'b':20})
# a=10
# b = 11
# c = 'hello'
# s = "{} {} {}".format(a,b,c)
# s = "{a} {b} {c}".format(b=True,c='lll',a=30)
# s = "{a} {b} {c}".format(**{'a':5.6,'b':20,'c':[1,2,3]})
# print(s)
# t1 = ('sno','sclass','sname')
# print(','.join(t1))
l1 = ','.join([key+"="+str(value) for key,value in {'sno':'009','sname':'jerry','sage':20}.items()])
print(l1)