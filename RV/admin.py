from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


class UserData(ModelAdmin):
    list_display = ['name', 'email', 'phone']


admin.site.register(UserProfile, UserData)