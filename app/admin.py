from django.contrib import admin

# Register your models here. 
from .models import User
from .models import User_task
admin.site.register(User)
admin.site.register(User_task)
