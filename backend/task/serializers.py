from unicodedata import category
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, Todo



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email',]

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','task_title']

class TodoSerializer(serializers.ModelSerializer):
    category = serializers.CharField(help_text="Task category like Reading, Office Tasks.....")
    class Meta:
        model = Todo
        fields = ['id','category','title','description','date']


    def create(self, validated_data):
        task_id = validated_data.pop('category')
        task_instance = Task.objects.get(id=task_id)
        todo = Todo.objects.create(**validated_data,category=task_instance)
        return todo
