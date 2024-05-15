from rest_framework import serializers
from .models import TodoList


class TodoListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=255)
    date = serializers.DateTimeField(read_only=True)
    completed = serializers.BooleanField(read_only=True)

