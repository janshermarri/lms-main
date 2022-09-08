from statistics import mode
from rest_framework import serializers
from lms_main import models
from lms_main.models import Teacher, Student
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'address', 'contact', 'qualifications']


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'user', 'address', 'contact', 'guardian']
