import uuid

from django.conf import settings
from django.db import models


class Profile(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30)
    bio = models.TextField(default="...")
    profile_image = models.ImageField(upload_to=".", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(
        "self", symmetrical=False, related_name="following"
    )

    def __str__(self):
        return self.nickname

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)

    def check_follow(self, user):
        return self.following.filter(pk=user.pk).exists()
