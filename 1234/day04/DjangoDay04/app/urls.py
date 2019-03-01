from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^basedemo/$', views.basedemo, name='basedemo'),
    url(r'^includedemo/$', views.includedemo, name='includedemo'),
    url(r'^home/$', views.home, name='home'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^mine/$', views.mine, name='mine'),

    url(r'^loginview/$', views.loginview, name='loginview'),
    url(r'^login/$', views.login, name='login'),
    url(r'^verifycode/$', views.verifycode, name='verifycode'),
]