from weakref import proxy
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class UserData(AbstractUser):
    class Users(models.TextChoices):
        ADMIN='ADMIN','Administer'
        STUDENT='STUDENT','Student'
    usertype=models.CharField('User',max_length=100,choices=Users.choices,default=Users.STUDENT)


class AdminManager(UserManager):
    def get_queryset(self):
        return super().get_queryset(*args,**kwargs).filter(usertype=UserData.Users.ADMIN)

class StudentManager(UserManager):
    def get_queryset(self):
        return super().get_queryset(*args,**kwargs).filter(usertype=UserData.Users.STUDENT)


class Admin(UserData):
    class Meta:
        proxy=True
    objects=AdminManager()

class Student(UserData):
    class Meta:
        proxy=True
    objects=StudentManager()