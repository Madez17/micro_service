from rest_framework import serializers
from .models import User, User_task

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'tasks'
        )

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_task
        fields = (
            'id',
            'description',
            'state',
            'user_id'    
        )
