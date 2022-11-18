from todoapp.models import ToDoList,ToDoItem
from todoapp.serializers import ToDoItemSerializer, TodoListSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Todo_List_Api(APIView):

    
    def get(self, request, format=None):
        todolists = ToDoList.objects.all()
        serializer = TodoListSerializer(todolists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Todo_Det_Api(APIView):
    def get_object(self, pk):
        try:
            return  ToDoList.objects.get(pk=pk)
        except  TodoList.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        ToDoList = self.get_object(pk)
        serializer = TodoListSerializer(ToDoList)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        ToDoList = self.get_object(pk)
        serializer = TodoListSerializer(ToDoList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ToDoList = self.get_object(pk)
        ToDoList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class Todoitem_Api(APIView):

    
    def get(self, request, format=None):
        TodoItem = ToDoItem.objects.all()
        serializer = ToDoItemSerializer(TodoItem, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToDoItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Todoitem_Det_Api(APIView):
    def get_object(self, pk):
        try:
            return  ToDoItem.objects.get(pk=pk)
        except  ToDoItem.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        ToDoItem = self.get_object(pk)
        serializer = ToDoItemSerializer(ToDoItem)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        ToDoItem = self.get_object(pk)
        serializer = ToDoItemSerializer(ToDoItem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        ToDoItem = self.get_object(pk)
        ToDoItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
 #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       
        
