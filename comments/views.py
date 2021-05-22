from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsWriterOrReadOnly


class CommentList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, webtoon_id, episode_id, format=None):
        comments = Comment.objects.filter(episode_info_id=episode_id).order_by(
            "-created_at"
        )
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, webtoon_id, episode_id, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(episode_info_id=episode_id, writer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsWriterOrReadOnly]

    def get_object(self, webtoon_id, episode_id, comment_id):
        return get_object_or_404(Comment, pk=comment_id, episode_info_id=episode_id)

    def get(self, request, webtoon_id, episode_id, comment_id, format=None):
        comment = self.get_object(webtoon_id, episode_id, comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, webtoon_id, episode_id, comment_id, format=None):
        comment = self.get_object(webtoon_id, episode_id, comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
