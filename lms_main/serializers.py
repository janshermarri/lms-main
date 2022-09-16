from rest_framework import serializers
from lms_main.models import Teacher, Student, Comment, TeacherStudentSession
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['first_name'] = user.first_name
        token['last_nams'] = user.last_name
        token['group'] = user.groups.all()[0].name

        return token
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

class TeacherStudentSessionSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    class Meta:
        model = TeacherStudentSession
        fields = ['id', 'teacher', 'student']

class CommentSerializer(serializers.ModelSerializer):
    teacher_student_session = TeacherStudentSessionSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'created_by', 'teacher_student_session', 'comments']
