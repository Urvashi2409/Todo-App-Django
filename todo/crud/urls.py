from django.urls import path
from . import views 

urlpatterns = [
    path('', views.todo_list, name="todo_list"),
    path('add/', views.add_todo, name="add_todo"),
    path("update/<int:pk>/", views.update_todo, name="update_todo"),
    path("delete/<int:pk>/", views.delete_todo, name="delete_todo"),
]

# "" - 127:0:0:1:8000 
# create a todo(add a new todo) 
# delete todo
# show todos 
# update todo

# . stands for current working directory


