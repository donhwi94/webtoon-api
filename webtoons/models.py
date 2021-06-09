from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class MainGenre(models.Model):
    name = models.CharField(max_length=10)
    sub_genre = models.ManyToManyField("SubGenre", through="Genre")

    def __str__(self):
        return self.name


class SubGenre(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Genre(models.Model):
    main_genre = models.ForeignKey(MainGenre, on_delete=models.CASCADE)
    sub_genre = models.ForeignKey(SubGenre, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.main_genre) + "/" + str(self.sub_genre)


class AgeRating(models.Model):
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.rating


class Webtoon(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        default="media/default_thumnail_image.jpeg", upload_to="webtoons/"
    )
    author = models.CharField(max_length=20)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    description = models.TextField()
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)
    age_rating = models.ForeignKey("AgeRating", on_delete=models.CASCADE)
    star_rating = models.FloatField()
    likes = models.PositiveIntegerField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Episode(models.Model):
    webtoon_info = models.ForeignKey("Webtoon", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.ImageField(
        default="media/default_episode_image.jpeg", upload_to="episodes/"
    )
    star_rating = models.FloatField(
        validators=[MinValueValidator(0.00), MaxValueValidator(10.00)]
    )
    likes = models.PositiveIntegerField()
    note = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title
