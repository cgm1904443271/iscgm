from django.db import models


'''
# 字段类型
- CharField 字符串
- IntegerField  整形
- AutoField 自增长(整形)
- FloatField 浮点数
- TextField 字符串(大文本)
- BooleanField 布尔类型
- DateField   日期
- TimeField   时间
- DateTimeField 时间和日期
- DecimalField 指定小数长度

# 约束
- primary_key 主键
- max_length    最大长度
- null  是否为空(默认是不能为空  null)
- auto_now 每次更新的时间
- auto_now_add 被创建时的时间
- decimal_places 小数点保留几位
- max_digits 总长度
- blank 是否为空白
- default 默认值

# 关系
- OneToOneField: 一对一
- ForeginKey: 一对多
- ManyToManyField: 多对多
'''
class Student(models.Model):
    # 假如有设置主键，系统就不会帮你添加
    # 假如没有设置主键，系统默认添加 id(主键、自增长)
    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=100)
    s_score = models.IntegerField(null=True)
    s_weight = models.FloatField(null=True)
    s_height = models.DecimalField(max_digits=6, decimal_places=1)
    s_detail = models.TextField(default='')
    s_delete = models.BooleanField(default=False)
    s_create = models.DateTimeField(auto_now_add=True)
    s_change = models.DateTimeField(auto_now=True)
    s_test = models.IntegerField(null=True)

    s_math = models.IntegerField(default=0)
    s_english = models.IntegerField(default=0)

    class Meta: # 元选项
        db_table = 'student'
        # 系统默认情况下，按id升序
        ordering = ['s_score']