import random

from django.db.models import Max, Avg, Q, F
from django.http import HttpResponse
from django.shortcuts import render

from meituan.models import Student


def index(request):
    return HttpResponse('首页 | 美团')


def cart(request):
    return HttpResponse('购物车 | 美团')


def addstu(request):
    stu = Student()
    stu.s_name = str(random.randrange(1,10000)) + '-zyz'
    stu.s_score = random.randrange(1,100)
    stu.s_weight = 75.00000022211
    stu.s_height = 180.33333333
    stu.s_detail = 'hello world!'
    stu.s_math = random.randrange(1,100)
    stu.s_english = random.randrange(1,100)

    # 数据存储
    stu.save()

    return HttpResponse('添加学生成功:' + stu.s_name)


def changestu(request):
    stu = Student.objects.get(pk=1)
    stu.s_name = str(random.randrange(1,10000)) + '-atom'
    stu.save()

    return HttpResponse('更新学生信息')


# 结果集
def showstudents(request):

    # 获取所有学生信息
    # all() 所有数据
    students = Student.objects.all()

    # filter() 符合要求的数据
    # id == 3的
    # students = Student.objects.filter(s_id=3)
    # id < 3的
    # students = Student.objects.filter(s_id__lt=3)
    # score >= 60
    # students = Student.objects.filter(s_score__gte=60)
    # id>3  且  成绩<60
    # students = Student.objects.filter(s_id__gt=3).filter(s_score__lt=60)
    # students = Student.objects.filter(s_id__gt=3, s_score__lt=60)

    # exclude() 过滤的符合要求的
    # 不显示id为3的
    # students = Student.objects.exclude(s_id=3)

    # 模糊查询
    # 名字以7开头
    # students = Student.objects.filter(s_name__startswith=7)
    # 名字以m结尾
    # students = Student.objects.filter(s_name__endswith='m')
    # 带有8的
    # students = Student.objects.filter(s_name__contains=8)

    # 排序
    # students = Student.objects.order_by('s_score')  # 升序
    # students = Student.objects.order_by('-s_score') # 降序

    # in
    # id 为 1,2,3,7,9
    # students = Student.objects.filter(s_id__in=[1,2,3,7,9])

    # 切片
    # students = Student.objects.all()[0:4]
    # students = Student.objects.order_by('-s_score')[0:3]

    # 显示学生信息
    student_str = ''
    for stu in students:
        student_str += '<p> {}-姓名:{},成绩:{},体重:{},身高:{} ,数学:{}, 英语:{}</p>'.format(stu.s_id, stu.s_name, stu.s_score, stu.s_weight, stu.s_height, stu.s_math, stu.s_english)

    return HttpResponse(student_str)


def showstu(request):
    # get() 符合要求的
    # id == 3
    # stu = Student.objects.get(s_id=3)
    # pk 是 primary_Key
    # stu = Student.objects.get(pk=3)
    # 如果数据有多个，抛出 'MultipleObjectsReturned'
    # stu = Student.objects.get(s_score=99)
    # 如果数据不存在， 抛出 'DoesNotExists'
    # stu = Student.objects.get(pk=100)

    # first()
    # stu = Student.objects.first()
    # stu = Student.objects.filter(pk=3).first()

    # last()
    # stu = Student.objects.last()

    # count() 个数
    # exists() 是否存在
    students = Student.objects.filter(pk=10)
    if students.exists():
        stu = students.first()
        # stu = students[0]
        stu_str = '<p> {}-姓名:{},成绩:{},体重:{},身高:{} </p>'.format(stu.s_id, stu.s_name, stu.s_score, stu.s_weight,stu.s_height)
        return HttpResponse(stu_str)
    else:
        return HttpResponse('该学员不存在')

    # stu_str = '<p> {}-姓名:{},成绩:{},体重:{},身高:{} </p>'.format(stu.s_id, stu.s_name, stu.s_score, stu.s_weight,stu.s_height)
    # return HttpResponse(stu_str)


def agg(request):
    # Max()、Min()、Avg()...
    # 求最大值
    # maxDir = Student.objects.aggregate(Max('s_score'))
    # # 最高分的学生信息
    # students = Student.objects.filter( s_score = maxDir['s_score__max'] )
    #
    # student_str = ''
    # for stu in students:
    #     student_str += '<p> {}-姓名:{},成绩:{},体重:{},身高:{} </p>'.format(stu.s_id, stu.s_name, stu.s_score, stu.s_weight,stu.s_height)
    #
    # return HttpResponse(student_str)

    # id 为 [1,2,3] 的平均成绩
    avgDir = Student.objects.filter(s_id__in=[1,2,3]).aggregate(Avg('s_score'))

    return HttpResponse('id为1,2,3 的学生平均分：' + str(avgDir['s_score__avg']))

# id大于15 或 成绩小于30
# filter(pk__gt=15).filter(s_score__lt=30)
def qtest(request): #   Q对象
    # Q对象，将条件进行封装
    # & 与
    # | 或
    # ~ 非

    # id大于15 或 成绩小于30
    # Q(s_id__gt=15)
    # Q(s_score__lt=30)
    # students = Student.objects.filter( Q(s_id__gt=15) | Q(s_score__lt=30) )

    # id>3  且  成绩<60
    # Q(s_id__gt=3)
    # Q(s_score__lt=60)
    students = Student.objects.filter( Q(s_id__gt=3) & Q(s_score__lt=60) )

    # 不显示id为3的
    # Q(s_id=3)
    # ~Q(s_id=3)
    students = Student.objects.filter(~Q(s_id=3))

    student_str = ''
    for stu in students:
        student_str += '<p> {}-姓名:{},成绩:{},体重:{},身高:{} </p>'.format(stu.s_id, stu.s_name, stu.s_score, stu.s_weight,stu.s_height)

    return HttpResponse(student_str)


def ftest(request):
    # F对象，自己和自己比较
    # 英语成绩 大于 数学成绩 的学生信息
    students = Student.objects.filter(s_english__gt=F('s_math'))

    student_str = ''
    for stu in students:
        student_str += '<p> {}-姓名:{},成绩:{},体重:{},身高:{} ,数学:{}, 英语:{}</p>'.format(stu.s_id, stu.s_name, stu.s_score,stu.s_weight, stu.s_height, stu.s_math,stu.s_english)

    return HttpResponse(student_str)