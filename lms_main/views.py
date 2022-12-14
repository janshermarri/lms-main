from lms_main.models import Teacher, Student, Comment, TeacherStudentSession
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from lms_main.serializers import TeacherSerializer, StudentSerializer, CommentSerializer, TeacherStudentSessionSerializer, MyTokenObtainPairSerializer
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import Group

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def create(self, request, *args, **kwargs):
        teacher_group = Group.objects.get(name='teacher')
        user = get_user_model().objects.create_user(
            first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], username=request.data['username'], password=request.data['password'],)
        user.groups.add(teacher_group)
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
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        student_group = Group.objects.get(name='student')
        user = get_user_model().objects.create_user(
            first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], username=request.data['username'], password=request.data['password'],)
        user.groups.add(student_group)
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


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        records = {}
        user_group = request.user.groups.all()[0].name
        if user_group == 'admin':
            records = Comment.objects.all()
        if user_group == 'teacher':
            records = Comment.objects.filter(
                teacher_student_session__teacher__user__id=request.user.id)
        if user_group == 'student':
            records = Comment.objects.filter(
                teacher_student_session__student__user__id=request.user.id)
        comments = CommentSerializer(records, many=True)
        return JsonResponse({'records': comments.data})

    def create(self, request, *args, **kwargs):
        comment = Comment.objects.create(
            teacher_student_session_id=request.data['session_id'], 
            comments=request.data['comments'],
            created_by_id=request.user.id
            )
        new_record = CommentSerializer(comment)
        return JsonResponse({"new_record": new_record.data, "status": "new record success"})

    def perform_create(self, serializer):
        serializer.save()


class TeacherStudentSessionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = TeacherStudentSession.objects.all()
    serializer_class = TeacherStudentSessionSerializer

    def list(self, request, *args, **kwargs):
        records = {}
        user_group = request.user.groups.all()[0].name
        if user_group == 'admin':
            records = TeacherStudentSession.objects.all()
        if user_group == 'teacher':
            records = TeacherStudentSession.objects.filter(
                teacher__user__id=request.user.id)
        if user_group == 'student':
            records = TeacherStudentSession.objects.filter(
                student__user__id=request.user.id)
        sessions = TeacherStudentSessionSerializer(records, many=True)
        return JsonResponse({'records': sessions.data})

    def create(self, request, *args, **kwargs):
        teacher_student_session = TeacherStudentSession.objects.create(
            teacher_id=request.data['teacher_id'], student_id=request.data['student_id'])
        new_record = TeacherStudentSessionSerializer(teacher_student_session)
        return JsonResponse({"new_record": new_record.data, "status": "new record success"})

    def perform_create(self, serializer):
        serializer.save()
