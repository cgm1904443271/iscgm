from django.conf.urls import url

from meituan import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cart/$', views.cart),

    url(r'^addstu/$', views.addstu),
    url(r'^changestu/$', views.changestu),
    url(r'^showstudents/$', views.showstudents),
    url(r'^showstu/$', views.showstu),
    url(r'^agg/$', views.agg),

    url(r'^qtest/$', views.qtest),
    url(r'^ftest/$', views.ftest),
]