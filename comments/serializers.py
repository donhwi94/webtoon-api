from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    episode_info = serializers.ReadOnlyField(source="episode_info.title")
    writer = serializers.ReadOnlyField(source="writer.username")

    class Meta:
        model = Comment
        fields = [
            "id",
            "episode_info",
            "writer",
            "contents",
            "created_at",
            "likes",
            "dislikes",
        ]
