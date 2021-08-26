from django.contrib import admin
from .models import courses_table


# Register your models here.

class course_admin(admin.ModelAdmin):
    list_display = ['c_id', 'c_name', 'c_fee', 'c_duration']


admin.site.register(courses_table, course_admin)


# class LogInPageAdmin(admin.ModelAdmin):
#     list_display = ['first_name', 'last_name', 'mobile_no']


# admin.site.register(LogInPage, LogInPageAdmin)
