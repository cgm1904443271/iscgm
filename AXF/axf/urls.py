from django.conf.urls import url

from axf import views

urlpatterns=[
    url(r'^home/$',views.home,name='home'),
    url(r'^market/$',views.market,name='market'),
    url(r'^market/(?P<childid>\d+)(?P<sortid>\d+)/$',views.market,name='marketson'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^checkusername/$',views.checkusername,name='checkusername'),

    url(r'^addcart/$',views.addcart,name='addcart')
]