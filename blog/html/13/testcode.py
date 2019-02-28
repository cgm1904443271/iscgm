import re

path = "student/12/34"
res = re.match(r'^student/(\d+)/(\d+)$',path,re.I)
print(res.groups())

def test(request,sno,sname):
    print(request,sno,sname)

test("ddd",*(11,22))
# s1 = ['name=tom','password=123']
# s1 = {key:value  for key,value in [value.split('=') for value in s1]}
# print(s1)