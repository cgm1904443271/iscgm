
import time

# 作业2: 爬取糗事百科文本页的所有段子,结果如 : xx说: xxxx
# https://www.qiushibaike.com/text/page/1/   # 1表示页码

# 正则表达式提示： 
#	# 获取一个评论
#   regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
#	# 获取名称
#   nameCom = re.compile('<h2>(.*?)</h2>', re.S)
#	# 获取内容
#	contentCom = re.compile('<span>(.*?)</span>', re.S)

import re
import urllib.request

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}

url = 'https://www.qiushibaike.com/text/page/1/ '


req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')

path = r'/home/misaka/PycharmProjects/PaChong/day02/'

regCom = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">', re.S)
regComs =regCom.findall(html)
for i in regComs:
    name_re = '<h2>(.*?)</h2>'
    name_res = re.compile(name_re,re.S)
    names = name_res.findall(i)[0]

    content_re = '<span>(.*?)</span>'
    content_res = re.compile(content_re,re.S)
    contents = content_res.findall(i)[0]

    xxx=names.strip()+ '说:'+'\n'+ contents.lstrip()
    with open(path+'qs.txt','a+') as fp:
        fp.write(xxx)









