from django.contrib import admin
from .models import Student, EmployeeModel, Course, CourseDetails


# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll', 'city')


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('emp_name', 'email', 'salary')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',)


@admin.register(CourseDetails)
class CourseDetailsAdmin(admin.ModelAdmin):
    list_display = ('cname', 'level', 'duration', 'fees')
