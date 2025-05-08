from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Province



admin.site.unregister(Group)
admin.site.register(Province)
admin.site.register(User)
# admin.site.register(Site)
