from django.shortcuts import render
from rest_framework import generics
from .models import Community
from .serializers import CommunitySerializer
from .permissions import IsCommunityAdmin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class CommunityListCreate(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        community = serializer.save()
        user = self.request.user
        community.members.add(user)
        community.admin = user
        community.save()
        
class CommunityRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [IsAuthenticated, IsCommunityAdmin]
