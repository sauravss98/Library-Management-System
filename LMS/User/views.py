from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from LMS.User.models import Student
from User.permissions import IsAdmin
from User.serializers import UserSerializer
# Create your views here.
class ListStudents(generics.ListAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer
    queryset = Student.objects.all()

class CreateStudent(generics.CreateAPIView):
    permission_classes=(IsAdmin,)
    serializer_class=UserSerializer