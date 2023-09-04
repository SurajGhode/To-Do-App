from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
    path('complete_task/<int:pk>/', views.complete_task, name='complete_task'),
    path('set_reminder/<int:pk>/', views.set_reminder, name='set_reminder'),
]
