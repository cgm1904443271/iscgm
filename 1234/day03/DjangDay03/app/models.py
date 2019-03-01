from django.db import models
from django.db.models import Manager

# 自定义管理器
class AnimalManager(Manager):
    # 重写
    def all(self):
        return super().all().exclude(is_del=True)

class Animal(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    # 逻辑删除
    is_del = models.BooleanField(default=False)

    # 如果没有自定义，系统默认 objects
    # objects = models.Manager()
    myObjects = AnimalManager()



#### 学习目标s: 明确不同的关系，不同的关系是如何实现的，数据删除时要怎么处理
## 一对一
# 人 和 身份证 【一个人 对应 一个身份证（身份证号）】
# 主表
class Person(models.Model):
    p_name = models.CharField(max_length=40)


# 身份证
# 从表(声明关系)
'''
create table app_idcard
(
  id          int auto_increment
    primary key,
  i_no        varchar(40)  not null,
  i_sex       int          not null,
  i_addr      varchar(100) not null,
  i_person_id int          not null,
  constraint i_person_id
  unique (i_person_id),
  constraint app_idcard_i_person_id_c24e2938_fk_app_person_id
  foreign key (i_person_id) references app_person (id)
);


主表数据删除， 关联的从表数据，默认是会被删除!
'''
class IDCard(models.Model):
    # 身份证号
    i_no = models.CharField(max_length=40)
    # 性别 (1男，2女)
    i_sex = models.IntegerField()
    # 地址
    i_addr = models.CharField(max_length=100)

    # 声明关系 [这个身份证是属于哪个人的]
    i_person = models.OneToOneField(Person)


    # 删除模式
    # 默认 models.CASCADE 模式
    # 主数据删除，有级联数据(从表)，级联数据也会被删除
    # 主数据删除，没有级联数据(从表)，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.CASCADE)

    # models.PROTECT 保护模式
    # 主表数据删除，有级联数据，抛出 'ProtectedError'
    # 主表数据删，没有级联数据，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.PROTECT)

    # models.SET_NULL 置空模式
    # 主表数据删除，有级联数据，将级联数据中关系字段设置为null
    # 主表数据删，没有级联数据，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.SET_NULL, null=True)

    # models.SET_DEFAULT 设置默认值模式
    # 主表数据删除，有级联数据，将级联数据中关系字段设置为 默认值
    # 主表数据删，没有级联数据，主表数据直接删除
    # i_person = models.OneToOneField(Person, models.SET_DEFAULT, default=1)



## 一对多
# 一个班级 对应 多个学生
# 主表
class Grade(models.Model):
    g_name = models.CharField(max_length=40)


# 从表(声明关系)
'''
create table app_student
(
  id         int auto_increment
    primary key,
  s_name     varchar(40) not null,
  s_age      int         not null,
  s_grade_id int         not null,
  constraint app_student_s_grade_id_129e1bc3_fk_app_grade_id
  foreign key (s_grade_id) references app_grade (id)
);
'''
class Student(models.Model):
    s_name = models.CharField(max_length=40)
    s_age = models.IntegerField()

    # 声明关系 (这学生 属于 哪个班)
    s_grade = models.ForeignKey(Grade, models.SET_NULL, null=True)



## 多对多
# 用户 和 商品 多对多
# 一个用户 对应 多个商品(购物车)
# 一个商品 对应 被多个用户收藏
# 主表
class User(models.Model):
    u_name = models.CharField(max_length=40)


# 从表(声明关系)
class Goods(models.Model):
    g_name = models.CharField(max_length=40)
    g_price = models.IntegerField()

    # 多对多关系
    g_collection = models.ManyToManyField(User)

# 关系表(系统帮我们维护， 后续都是我们自己手动维护)
'''
create table app_goods_g_collection
(
  id       int auto_increment
    primary key,
  goods_id int not null,
  user_id  int not null,
  constraint app_goods_g_collection_goods_id_user_id_79e182fc_uniq
  unique (goods_id, user_id),
  constraint app_goods_g_collection_goods_id_cc3a7ad8_fk_app_goods_id
  foreign key (goods_id) references app_goods (id),
  constraint app_goods_g_collection_user_id_ce13ea95_fk_app_user_id
  foreign key (user_id) references app_user (id)
);
'''
