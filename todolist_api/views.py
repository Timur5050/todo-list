from rest_framework import generics
from .serializers import TodoListSerializer
from .models import TodoList


# Create your views here.
class TodoListAPIView(generics.ListAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListAPIPost(generics.CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListUpdate(generics.UpdateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListDelete(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    