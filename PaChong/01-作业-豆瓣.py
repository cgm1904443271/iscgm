


# 作业1 : 分页获取豆瓣的数据（json数据）， 把电影图片存入本地，且图片名取电影名
# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start="+ str(i * 20)+"&limit=20"
import json
import urllib.request
import os

path = r'/home/misaka/PycharmProjects/PaChong/day02/img'

headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
}

x = 0
for i in range(1, 3):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(i * 20) + "&limit=20"

    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    context = response.read().decode()

    json_list = json.loads(context)
    # print(json_list)

    # print(cover_url)
    for item in json_list:
        cover_url = item['cover_url']
        file_name = item['title']
        x += 1
        urllib.request.urlretrieve(cover_url,'/home/misaka/PycharmProjects/PaChong/day02/img/'+file_name+'.jpg')
        print(x,'下载中')














