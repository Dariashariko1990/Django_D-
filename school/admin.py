from django.contrib import admin

from .models import Student, Teacher


class StudentsInline(admin.TabularInline):
    model = Student.teacher.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [StudentsInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [StudentsInline]
