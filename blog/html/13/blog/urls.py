import re
import views
urlpatterns = [
    (r'^$',views.index),
    (r'^login$',views.login),
    (r'^dologin$',views.doLogin),
    (r'^logout$',views.logout),
    (r'^studentlist$',views.studentList),
    (r'^student/(\d+)$',views.studentInfo),
    (r'^register$',views.register),
    (r'^static/',views.loadStatic),
    (r'^yzm',views.yzm),
    (r'^test$',views.test),
    (r'^area$',views.area),
    (r'^province/(\d+)',views.province),
    (r'^hello$',views.hello),
    (r'^jsonp/(\d+)/(\w+)$',views.jsonp),
    (r'^ajax$',views.ajax),
    (r'^get$',views.get),
]