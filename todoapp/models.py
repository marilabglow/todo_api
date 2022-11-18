from django.db import models

from django.utils import timezone



def one_week_hence():
    return timezone.now() + timezone.timedelta(days=30)




class ToDoList(models.Model):
    title = models.CharField(max_length=100, unique=True)

class ToDoItem(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    tasktitle = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    

    class Meta:
        ordering = ["due_date"]
# Create your models here.
