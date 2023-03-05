from django.contrib import admin
from . models import Contact, AdminLogin
# Register your models here.
admin.site.register(Contact)
admin.site.register(AdminLogin)