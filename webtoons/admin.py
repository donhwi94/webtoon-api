from django.contrib import admin
from .models import Category, MainGenre, SubGenre, Genre, AgeRating, Webtoon, Episode

admin.site.register(Category)
admin.site.register(MainGenre)
admin.site.register(SubGenre)
admin.site.register(Genre)
admin.site.register(AgeRating)
admin.site.register(Webtoon)
admin.site.register(Episode)
