from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from webtoons.models import Category, Webtoon, Episode
from webtoons.serializers import CategorySerializer,WebtoonDetailSerializer, EpisodeDetailSerializer

# 요일별 웹툰 전체 목록 조회
class WebtoonList(APIView):
    def get(self, request, format=None):
        webtoons = Category.objects.all()
        serializers = CategorySerializer(webtoons, many=True)
        return Response(serializers.data)

# 웹툰 별 회차 목록 조회
class WebtoonDetail(APIView):
    def get(self, request, webtoon_id, format=None):
        webtoon = get_object_or_404(Webtoon, pk=webtoon_id)
        serializer = WebtoonDetailSerializer(webtoon)
        return Response(serializer.data)

# 웹툰 회차 상세 조회 
class EpisodeDetail(APIView):
    def get(self, request, webtoon_id, episode_id, format=None):
        episode = get_object_or_404(Episode, webtoon_info_id=webtoon_id, pk=episode_id)
        serializer = EpisodeDetailSerializer(episode)
        return Response(serializer.data)
