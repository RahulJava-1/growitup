from django.urls import path
from . import views
app_name="adminzone"
urlpatterns = [
    path('home/',views.home,name='home'),
    path('customer',views.customer,name='customer'),
    path('logout', views.logout,'logout'),
    path('achangepassword',views.achangepassword,name='achangepassword'),
    path('adminchangepwd',views.adminchangepwd,name='adminchangepwd'),
    path('deletecust/(?P<id>\d+)$',views.deletecust,name='deletecust'),
]
