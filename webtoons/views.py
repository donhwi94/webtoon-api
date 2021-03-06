from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from webtoons.models import Category, Webtoon, Episode
from webtoons.serializers import (
    CategorySerializer,
    WebtoonSerializer,
    WebtoonDetailSerializer,
    EpisodeDetailSerializer,
)

# API 단일 진입점
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "webtoons": reverse("webtoon-list", request=request, format=format),
            "interests": reverse("interest-list", request=request, format=format),
        }
    )


# 요일별 웹툰 전체 목록 조회
class WebtoonList(APIView):
    def get(self, request, format=None):
        # 검색 조건이 있으면 조건에 해당하는 웹툰 리스트 목록을 출력
        if request.query_params:
            search_param = self.request.query_params.get("search", default="")
            webtoons = Webtoon.objects.filter(
                Q(author__icontains=search_param) | Q(title__icontains=search_param)
            ).distinct()
            serializer = WebtoonSerializer(webtoons, many=True)
            return Response(serializer.data)

        # 검색 조건이 없으면 요일별 웹툰 리스트 목록을 출력
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
