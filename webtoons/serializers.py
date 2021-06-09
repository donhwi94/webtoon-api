from rest_framework import serializers

from .models import Webtoon, Episode, Category, SubGenre, MainGenre, Genre, AgeRating


class SubGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubGenre
        fields = ["id", "name"]


class MainGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainGenre
        fields = ["id", "name"]


class GenreSerializer(serializers.ModelSerializer):
    main_genre = serializers.ReadOnlyField(source="maingenre.name")
    sub_genre = serializers.ReadOnlyField(source="subgenre.name")

    class Meta:
        model = Genre
        fields = ["id", "main_genre", "sub_genre"]


class AgeRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgeRating
        fields = ["id", "rating"]


class WebtoonSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    age_rating = serializers.ReadOnlyField(source="age_rating.rating")
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Webtoon
        fields = [
            "id",
            "title",
            "thumbnail",
            "author",
            "category",
            "description",
            "genre",
            "age_rating",
            "likes",
        ]


class CategorySerializer(serializers.ModelSerializer):
    webtoon_set = WebtoonSerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "name", "webtoon_set"]


class EpisodeSerializer(serializers.ModelSerializer):
    content = serializers.ImageField(use_url=True)

    class Meta:
        model = Episode
        fields = [
            "id",
            "title",
            "content",
            "star_rating",
            "likes",
            "note",
            "created_at",
        ]


class WebtoonDetailSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    age_rating = serializers.ReadOnlyField(source="age_rating.rating")
    episode_set = EpisodeSerializer(many=True)
    thumbnail = serializers.ImageField(use_url=True)

    class Meta:
        model = Webtoon
        fields = [
            "id",
            "title",
            "thumbnail",
            "author",
            "category",
            "description",
            "genre",
            "age_rating",
            "likes",
            "episode_set",
        ]


class EpisodeDetailSerializer(serializers.ModelSerializer):
    webtoon_info = serializers.ReadOnlyField(source="webtoon.title")
    content = serializers.ImageField(use_url=True)

    class Meta:
        model = Episode
        fields = [
            "id",
            "webtoon_info",
            "title",
            "content",
            "star_rating",
            "likes",
            "note",
            "created_at",
        ]
