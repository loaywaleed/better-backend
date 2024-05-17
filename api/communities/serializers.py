from rest_framework import serializers
from .models import Community
from ..authentication.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Community
        fields = "__all__"
