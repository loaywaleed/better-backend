from django.shortcuts import render
from rest_framework import generics
from .models import Community
from .serializers import CommunitySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommunityListCreate(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

