from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index),


    url(r'^animal/$', views.animal),
    url(r'^addanimal/$', views.addanimal),
    url(r'^selectanimal/$', views.selectanimal),
    url(r'^deleteanimal/$', views.deleteanimal),
    url(r'^updateanimal/$', views.updateanimal),


    url(r'^onetoone/$', views.onetoone),    # 一对一页面
    url(r'^addperson/$', views.addperson),  # 添加人
    url(r'^bindcard/$', views.bindcard),    # 绑定身份证
    url(r'^deleteperson/$', views.deleteperson),    # 删除人
    url(r'^deletecard/$', views.deletecard),    # 删身份证
    url(r'^getpersoncard/$', views.getpersoncard),  # 人获取身份证信息(主表获取从表信息)
    url(r'^getcardperson/$',views.getcardperson),   # 身份证 获取 人的信息(从表获取主表信息)


    url(r'^foreignkey/$', views.foreignkey),    # 页面
    url(r'^addgrade/$', views.addgrade),    # 添加班级
    url(r'^addstudent/$', views.addstudent),    # 添加学生
    url(r'^delgrade/$', views.delgrade),    # 删除班级
    url(r'^delstudent/$', views.delstudent),    # 删除学生
    url(r'^showgrade/$', views.showgrade),    # 获取班级 对应 学生
    url(r'^showstudents/$', views.showstudents),     # 获取学生 对应 班级信息


    url(r'^manytomany/$', views.manytomany),    # 页面
    url(r'^adduser/$', views.adduser),  # 添加用户
    url(r'^addgoods/$', views.addgoods),    # 添加商品
    url(r'^addcart/$', views.addcart),  # 添加购物车
    url(r'^showcart/$', views.showcart),    # 显示购物车
    url(r'^addcollect/$', views.addcollect),    # 添加收藏
    url(r'^showgoods/$', views.showgoods),  # 显示商品(收藏数量)
]
