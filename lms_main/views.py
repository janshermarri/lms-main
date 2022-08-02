from lms_main.models import Teacher, Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from lms_main.serializers import TeacherSerializer, StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer