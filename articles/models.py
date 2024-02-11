from turtle import mode
from django.db import models
from accounts.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, models.CASCADE)

    def __str__(self) -> str:
        return self.title
