from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', views.helloWorld),
    path('', views.taskList, name='task-list'),
    path('task/<int:id>', views.taskView, name='task-view'),
    path('newTask/', views.newTask, name='new-task'),
    path('editTask/<int:id>', views.editTask, name='edit-task'),
    path('deleteTask/<int:id>', views.deleteTask, name='delete-task')
]
