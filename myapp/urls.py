from django.urls import re_path,include
from . import views
app_name = "myapp"
urlpatterns = [
    re_path(r'^login',views.login,name='login'),
    re_path(r'^contact',views.contact,name='contact'),
    re_path(r'^validateadmin',views.validateadmin,name='validateadmin'),
]
