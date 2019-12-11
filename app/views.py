from django.shortcuts import render
from rest_framework import generics
from app.models import User, User_task
from app.serializers import UserSerializer, TaskSerializer

class UserList(generics.ListCreateAPIView):  
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTaskList(generics.ListCreateAPIView):  
    queryset = User_task.objects.all()
    serializer_class = TaskSerializer


class UserTaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_task.objects.all()
    serializer_class = TaskSerializer
