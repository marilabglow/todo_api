from django.urls import include,path
from todoapp import views
from .views import *
from django.contrib import admin
urlpatterns = [
   
    
    path('View_todolist', Todo_List_Api.as_view(),name='View_todolist'),
    path('det_todolist/<int:pk>/', Todo_Det_Api.as_view(),name='det_todolist'),
    
    path('todoitemlist', Todoitem_Api.as_view(),name='View_todolist'),
    path('Todoitem_Det_Api/<int:pk>/', Todoitem_Det_Api.as_view(),name='det_todolist'),
   
    
    
    
]