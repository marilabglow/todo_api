from django.contrib import admin
from .models import ToDoList,ToDoItem

class Todo_list_admin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(ToDoList,Todo_list_admin)
class Todo_item_admin(admin.ModelAdmin):
    list_display = ("todolist","tasktitle","description","created_date","due_date",)
admin.site.register(ToDoItem,Todo_item_admin)
