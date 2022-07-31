from django.db import models
from django.contrib.auth.models import User
from sqlalchemy import true

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    photo = models.ImageField( upload_to='./static/',blank=True,null=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=True)
    

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.title}({self.user.username})'