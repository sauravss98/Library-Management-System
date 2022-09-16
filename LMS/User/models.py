from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,BaseUserManager
# Create your models here.

class Usermanager(BaseUserManager):
    def _create_user(self, username, idNumber,password=None):
        if not username:
            raise ValueError("The given username must be set")
        if not idNumber:
            raise ValueError("The given idNumber must be set")
        
        user= self.model(
            username=username, 
            idNumber=idNumber,
        ) 
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,username,idNumber,password):
        user=self.create_user(
            username=username,
            idNumber=idNumber,
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_verified = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username  =models.CharField(max_length=55, unique=True)
    idNumber = models.IntegerField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False) # a superuser
    is_admin_request = models.BooleanField(default=False)

    USERNAME_FIELD = 'idNumber'
    REQUIRED_FIELDS = ['username'] # P

    objects =Usermanager()

    def __str__(self):
        return self.username

    def has_perm(self, perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True








# class UserData(AbstractUser):
#     class Users(models.TextChoices):
#         ADMIN='ADMIN','Administer'
#         STUDENT='STUDENT','Student'
#     usertype=models.CharField('User',max_length=100,choices=Users.choices,default=Users.STUDENT)


# class AdminManager(UserManager):
#     def get_queryset(self,*args,**kwargs):
#         return super().get_queryset(*args,**kwargs).filter(usertype=UserData.Users.ADMIN)

# class StudentManager(UserManager):
#     def get_queryset(self,*args,**kwargs):
#         return super().get_queryset(*args,**kwargs).filter(usertype=UserData.Users.STUDENT)


# class Admin(UserData):
#     class Meta:
#         proxy=True
#     objects=AdminManager()

# class Student(UserData):
#     class Meta:
#         proxy=True
#     objects=StudentManager()