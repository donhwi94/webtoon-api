from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Interest
from .serializers import InterestSerializer, InterestDetailSerializer

class InterestList(APIView):
    def get(self, request, format=None):
        interests = Interest.objects.filter(owner=request.user)
        serializer = InterestSerializer(interests, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = InterestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InterestDetail(APIView):
    def get_object(self, interest_id):
        return get_object_or_404(Interest, pk=interest_id)

    def get(self, request, interest_id, format=None):
        interest = self.get_object(interest_id)
        serializer = InterestDetailSerializer(interest)
        return Response(serializer.data)

    def delete(self, request, interest_id, format=None):
        interest = self.get_object(interest_id)
        interest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)