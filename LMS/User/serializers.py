from dataclasses import field
import email
from pyexpat import model
from turtle import mode
from rest_framework import serializers
from django.contrib.auth import get_user_model

UserData=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField()
    def create(self, validated_data):
            user=UserData.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password'],
            )
            return user
    
    def update(self, instance, validated_data):
        password=validated_data.pop('password')
        user=super().update(instance,validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
    
    class Meta:
        model=UserData
        fields=['id','email','username','password']