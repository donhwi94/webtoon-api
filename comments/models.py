from django.db import models
from webtoons.models import Episode


class Comment(models.Model):
    episode_info = models.ForeignKey(Episode, on_delete=models.CASCADE)
    writer = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

    def __str__(self):
        return self.contents
