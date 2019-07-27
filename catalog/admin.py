from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(students)
class AdminStudents(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'info')
    list_filter = ('math', 'astronomy', 'football')


@admin.register(Teacher)
class AdminTeacher(admin.ModelAdmin):
    list_display = ('name', 'cabinets')



@admin.register(Cabinet)
class AdminCabinet(admin.ModelAdmin):
    pass





