from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.likes import Likes
from ..serializers import LikeSerializer

# Create your views here.


class Like(APIView):
    def get(self, request):
        """Index Request"""
        likes = Likes.objects.all()[:10]
        data = LikeSerializer(likes, many=True).data
        return Response(data)

    serializer_class = LikeSerializer

    def post(self, request):
        """Post request"""
        print(request.data)
        like = LikeSerializer(data=request.data['likes'])
        if like.is_valid():
            b = like.save()
            return Response(like.data, status=status.HTTP_201_CREATED)
        else:
            return Response(like.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        like = get_object_or_404(Like, pk=pk)
        data = LikeSerializer(like).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        like = get_object_or_404(Like, pk=pk)
        ms = LikeSerializer(like, data=request.data['likes'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        like = get_object_or_404(Like, pk=pk)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
