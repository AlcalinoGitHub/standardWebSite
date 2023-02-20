from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=20)
    Content = models.TextField(default= '')
    Likes = models.IntegerField(default=0)
    Published = models.BooleanField(default=False)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    LikedBy = models.JSONField(default=list)
    Comments = models.JSONField(default=list)

