from django.urls import path
from .views import TodoListView, TodoView
urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:id>/', TodoView.as_view(), name='todo')
]
