from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "first_name", "last_name", "email"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserCommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "communities"]
        
        
class MemberSerializer(serializers.Serializer):
    email_or_username = serializers.CharField()

    def validate_email_or_username(self, value):
        """
        Check if the provided value is a valid email or username.
        """
        try:
            # Check if the value is a valid email address
            user = User.objects.get(email=value)
            return user
        except User.DoesNotExist:
            try:
                # Check if the value is a valid username
                user = User.objects.get(username=value)
                return user
            except User.DoesNotExist:
                raise serializers.ValidationError("User not found.")