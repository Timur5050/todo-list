from rest_framework import serializers
from .models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TodoList
        fields = ("id", "title", "date", "description", "completed", "user")  # "__all__"


