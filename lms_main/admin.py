from django.contrib import admin
from .models import Teacher, Student, Comment, TeacherStudentSession
# Register your models here.

admin.site.register([Teacher, Student, Comment, TeacherStudentSession])