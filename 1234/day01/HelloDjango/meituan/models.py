from django.db import models

# 学生 模型类
# 默认: appName_ModelName
class Student(models.Model):
    name = models.CharField(max_length=200)
    score = models.IntegerField()


# 用户 模型类
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)