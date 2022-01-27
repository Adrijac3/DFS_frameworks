from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.todoView),
    path('addTodoItem/', views.addTodoView),
    path('deleteTodoItem/<int:i>', views.deleteTodoView)
]