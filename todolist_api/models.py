from datetime import datetime

from django.db import models
from django.db.models import CASCADE


# Create your models here.
# class Users(models.Model):
#     login = models.CharField()
#     password = models.CharField()
#
#     def __str__(self):
#         return self.login


class TodoList(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    data = models.DateTimeField(default=datetime.now)
    completed = models.BooleanField(default=False)
    #user_id = models.ForeignKey(Users, on_delete=CASCADE, related_name='id')

    def __str__(self):
        return self.title
