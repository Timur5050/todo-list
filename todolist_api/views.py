from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import TodoListSerializer
from .models import TodoList


# Create your views here.
class TodoListAPIView(generics.ListAPIView):
    #queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return TodoList.objects.filter(user=user)


class TodoListAPIPost(generics.CreateAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated, )


class TodoListUpdate(generics.UpdateAPIView):
    #queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return TodoList.objects.filter(user=user)


class TodoListDelete(generics.DestroyAPIView):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    permission_classes = (IsAdminUser, )
