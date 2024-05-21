from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class TodoList(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# class Users(models.Model):
#     login = models.CharField()
#     password = models.CharField()
#
#     def __str__(self):
#         return self.login
