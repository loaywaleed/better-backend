from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Habit, Community
from django.contrib.auth.models import User
from .serializers import HabitSerializer, UserSerializer, CommunitySerializer


class HabitListCreate(generics.ListCreateAPIView):
    """
    A view for listing and creating Habits

    get:
    Return a list of all habits.

    post:
    Create a new habit instance.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, or deleting a single Habit

    get:
    Return the specified habit.

    put:
    Update the specified habit.

    delete:
    Delete the specified habit.
    """
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = "pk"


class UserCreate(generics.CreateAPIView):
    """
    A view for creating a new User object.

    post:
    Create a new user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CommunityListCreate(generics.ListCreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
