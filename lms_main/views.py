from statistics import quantiles
from lms_main.models import Teacher, Student
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from lms_main.serializers import TeacherSerializer, StudentSerializer, UserSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.create(
            first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], username=request.data['username'])
        teacher = Teacher.objects.create(
            user=user, address=request.data['address'], contact=request.data['contact'], qualifications=request.data['qualifications'])
        new_record = TeacherSerializer(teacher)
        return JsonResponse({"new_record": new_record.data, "status": "new record success"})

    def destroy(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('pk'))
            user.delete()
            return JsonResponse({"status": "delete record success"})
        except:
            return JsonResponse({"status": "delete record error"}, status=500)

    def perform_create(self, serializer):
        serializer.save()


class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.create(
            first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], username=request.data['username'])
        student = Student.objects.create(
            user=user, address=request.data['address'], contact=request.data['contact'], guardian=request.data['guardian'])
        new_record = StudentSerializer(student)
        return JsonResponse({"new_record": new_record.data, "status": "new record success"})

    def destroy(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=kwargs.get('pk'))
            user.delete()
            return JsonResponse({"status": "delete record success"})
        except:
            return JsonResponse({"status": "delete record error"}, status=500)

    def perform_create(self, serializer):
        serializer.save()
