from rest_framework import serializers

from .models import Interest


class InterestSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Interest
        fields = ["id", "owner", "interest_webtoon_list"]


class InterestDetailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    interest_webtoon_list = serializers.ReadOnlyField(
        source="interest_webtoon_list.title"
    )

    class Meta:
        model = Interest
        fields = ["id", "owner", "interest_webtoon_list"]
