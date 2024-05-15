from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TodoListSerializer
from .models import TodoList


# Create your views here.
class TodoListAPIView(APIView):
    def get(self, request):
        lst = TodoList.objects.all()
        return Response({"post": TodoListSerializer(lst, many=True).data})

    def post(self, request):
        serializer = TodoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = TodoList.objects.create(
            title=request.data['title'],
            description=request.data['description']
        )
        return Response({"new task": TodoListSerializer(post_new)})

