from django.contrib import admin
from .models import User,Student,Orders,Myinfo

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Orders)
admin.site.register(Myinfo)