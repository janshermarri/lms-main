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

class Comment(models.Model):
    user = models.ManyToManyField(User, related_name="comments")
    comments = models.TextField(blank=False)

    def __str__(self):
        return (self.user.first_name + " " + self.user.last_name + ": " + self.comments)