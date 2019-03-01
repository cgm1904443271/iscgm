from django.conf.urls import url

from meituan import views

urlpatterns = [
    # 路由规则 --> 视图函数
    url(r'^$', views.index),
    url(r'^index/$', views.index),

    url(r'^aaa/$', views.home),
    url(r'^bbb/$', views.home),

    url(r'^cart/$', views.cart),

    url(r'^addstu/$', views.addstu),
]