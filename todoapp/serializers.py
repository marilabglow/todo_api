from rest_framework import serializers
from .models import ToDoList,ToDoItem

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ["title",]
class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoItem
        fields = ["todolist","tasktitle","description","created_date","due_date",]
        