from django.db import models
from webtoons.models import Webtoon

class Interest(models.Model):
    owner = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    interest_webtoon_list = models.ForeignKey(Webtoon, on_delete=models.CASCADE)

    def __str__(self):
        return self.interest_webtoon_list.title
