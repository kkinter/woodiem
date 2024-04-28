from django.contrib.auth import get_user_model
from django.db import models

from .utils import calculate_read_time

User = get_user_model()


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self) -> str:
        return f"{self.title} - {self.author}"

    def read_time(self):
        return calculate_read_time(self)
