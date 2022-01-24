from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class EmployeeAdmin(UserAdmin):
    pass

admin.site.register(User, EmployeeAdmin)
