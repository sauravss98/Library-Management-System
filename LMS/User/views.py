from ast import Is
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from LMS.User.models import Student
from User.permissions import IsAdmin
from User.serializers import UserSerializer
# Create your views here.
class ListStudentsDetails(generics.ListAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer
    queryset = Student.objects.all()

class CreateStudentDetails(generics.CreateAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer

class UpdateStudentDetails(generics.UpdateAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer
    queryset=Student.objects.all()

class DeleteStudentDetails(generics.DestroyAPIView):
    permission_classes=(IsAdmin,)
    queryset=Student.objects.all()