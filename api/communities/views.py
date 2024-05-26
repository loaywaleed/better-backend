from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Community
from .serializers import CommunitySerializer
from .permissions import IsCommunityAdmin
from django.contrib.auth.models import User
from ..users.serializers import UserSerializer
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
    lookup_field = 'id'


class MemberAddAPIView(APIView):
    def _get_community(self, id):
        try:
            return Community.objects.get(id=id)
        except Community.DoesNotExist:
            raise NotFound({'error': 'Community does not exist'})
    
    def _get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound({'error': 'User does not exist'})
        
    def post(self, request, id):
        try:
            community = Community.objects.get(id=id)
        except Community.DoesNotExist:
            return Response({'error': 'Community does not exist'})
        username = request.data.get('username')
        if not username:
            raise ValidationError({'error': 'Username is required'})
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'})
        if user in community.members.all():
            return Response({'error': 'User is already a member of this community'})
        community.members.add(user)
        community.save()
        serializer = UserSerializer(user)
        return Response({'user added': serializer.data})
    
    def delete(self, request, id):
        community = self.get_community(id)
        username = request.data.get('username')
        if not username:
            return ValidationError({'error': 'Username is required'})
        user = self._get_user(username)
        if user not in community.members.all():
            return Response({'error': 'User is not a member of this community'})
        community.members.remove(user)
        community.save()
        return Response({'message': 'User removed from the community succesfully'})
    
