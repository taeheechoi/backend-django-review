from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Todo
# Create your views here.

class TodoListView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user)
    

class TodoView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Todo.objects.filter(created_by=self.request.user)

