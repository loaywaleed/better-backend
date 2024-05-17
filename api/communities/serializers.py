from rest_framework import serializers
from .models import Community
from ..users.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Community
        fields = "__all__"
