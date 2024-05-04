from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Habit
from django.contrib.auth.models import User
from .serializers import HabitSerializer, UserSerializer


class HabitListCreate(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = "pk"


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
