from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)
    qualifications = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)
    guardian = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name)

class TeacherStudentSession(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'Teacher: {self.teacher.user.first_name} {self.teacher.user.last_name}, Student: {self.student.user.first_name} {self.student.user.last_name}'


class Comment(models.Model):
    teacher_student_session = models.ForeignKey(TeacherStudentSession, related_name="session", on_delete=models.CASCADE)
    comments = models.TextField(blank=False)

    def __str__(self):
        return self.comments

