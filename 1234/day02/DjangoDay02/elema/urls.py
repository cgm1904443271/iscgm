from django.conf.urls import url

from elema import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^cart/$', views.cart),
]