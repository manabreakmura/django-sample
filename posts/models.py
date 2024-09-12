from django.db import models

from users.models import User


class Post(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ("-updated_at",)

    def __str__(self) -> str:
        return f"{self.user.username}: {self.title} ({self.created_at})"
