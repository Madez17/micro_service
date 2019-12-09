from django.db import models

# app/models.py
class User(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Task(models.Model):
    task = models.CharField(max_length=200)
    user_task = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.task
