## 一、自我介绍
	钟远智(钟哥)
	
## 二、笔记
	https://www.jianshu.com/u/44cde87b5c30

## 三、课程安排
```
- Django基本框架和流程
- 模型基本使用
- 模型高级使用
- 视图
- 模板
- 高级(站点管理、缓存)
- Django REST framework
- 爱鲜蜂(项目)
- 项目部署 
- 考试
```

## 四、学习方法
```
- 画图(流程、思路)
- 遇到问题(看错误提示、调试代码、分析问题)
```

## 五、Diango项目
```
- 创建
    django-admin startproject projectName

- 文件说明
    manage.py   命令行工具(项目入口)
    projectName/__init__.py   Python包
    projectName/settings.py   项目的配置文件
    projectName/urls.py       路由(URL)
    projectName/wsgi.py       项目部署(web服务器的入口)

- 项目启动
    python manage.py runserver
    python manage.py runserver 0.0.0.0:8000

- 创建应用
    python manage.py startapp appName

- 应用文件说明
    meituan/migrations    迁移目录(和模型数据库有关)
    meituan/__init__.py   python包
    meituan/admin.py      站点配置
    meituan/apps.py       应用配置
    meituan/models.py     模型
    meituan/tests.py      测试
    meituan/views.py      视图

- 注意
    创建完应用后，记得在settings.py文件中 INSTALLED_APPS 下 添加对应应用!
```
> Django自带有测试服务器!


## 六、模板配置
```
- 创建template目录
- settings.py中配置
    TEMPLATES = {
        'DIRS': [
            os.path.join(BASE_DIR, 'template')
        ],S
    }
```

## 七、数据库操作(迁移)
```
# 需要存储数据，数据库中必须有对应的表单
- 创建模型类
    class Student(models.Model):
        name = models.CharField(max_length=200)
        score = models.IntegerField()

- 生成迁移文件
    python manage.py makemigrations

- 执行迁移文件(执行完成之后，就会生成对应的表单)
    python manage.py migrate
```

## 八、存储数据
```
stu = Student()
stu.name = '张三'
stu.score = 100

stu.save()
```





