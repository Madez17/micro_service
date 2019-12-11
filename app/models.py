from django.db import models
# app/models.py
class User(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class User_task(models.Model):
    id = models.AutoField(primary_key = True)
    description = models.CharField(max_length=200)
    state = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.description
    def toggle_open_closed(self):
        self.state = not self.state
        self.save()
