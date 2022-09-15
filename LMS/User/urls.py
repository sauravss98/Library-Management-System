from django.urls import path
from rest_framework.authtoken import views as auth_views

from User import views

urlpatterns=[
    path('token-auth/', auth_views.obtain_auth_token),
    path('student/create')
]