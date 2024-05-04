from django.shortcuts import render
from rest_framework import generics
from .models import Habit
from .serializers import HabitSerializer


class HabitListCreate(generics.ListCreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    lookup_field = "pk"
