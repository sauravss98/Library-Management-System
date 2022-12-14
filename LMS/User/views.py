from ast import Is
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from User.models import User
from User.permissions import IsAdmin
from User.serializers import UserSerializer
# Create your views here.

class ListStudentsDetails(generics.ListAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer
    queryset = User.objects.filter(is_admin=False)

class CreateStudentDetails(generics.CreateAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer

class UpdateStudentDetails(generics.UpdateAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer
    queryset=User.objects.filter(is_admin=False)

class DeleteStudentDetails(generics.DestroyAPIView):
    permission_classes=(IsAdmin,)
    queryset=User.objects.filter(is_admin=False)

class StudentDetail(generics.RetrieveAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer
    queryset=User.objects.filter(is_admin=False)
