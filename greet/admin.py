from django.contrib import admin
from django.forms import models
from .models import PMProfile, DevProfile, User, Ticket
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(User)
admin.site.register(PMProfile)
admin.site.register(DevProfile)

# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'first_name', 'is_staff', 'is_active')

# admin.site.register(User)
admin.site.register(Ticket)