from rest_framework import serializers
from .models import Community, CommunityHabit
from ..users.serializers import UserSerializer



class HabitSerializer(serializers.ModelSerializer):   
    class Meta:
        model = CommunityHabit
        fields = ['id', 'name', 'description', 'motivation', 'frequency', 'duration']

class CommunitySerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, read_only=True)
    habits = HabitSerializer(many=True, read_only=True)
    class Meta:
        model = Community
        fields = "__all__"
