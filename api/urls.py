from django.urls import path
from . import views

urlpatterns = [
    path('habits/',
         views.HabitListCreate.as_view(),
         name="habit-view-create"),
    path('habits/<int:pk>/',
         views.HabitRetrieveUpdateDestroy.as_view(),
         name="habit-update-destroy"),
]
