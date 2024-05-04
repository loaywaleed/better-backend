from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('habits/',
         views.HabitListCreate.as_view(),
         name="habit-view-create"),
    path('habits/<int:pk>/',
         views.HabitRetrieveUpdateDestroy.as_view(),
         name="habit-update-destroy"),
    path('users/signup/',
         views.UserCreate.as_view(),
         name="user-create"),
    path('token/',
         TokenObtainPairView.as_view(),
         name="token-view"),
    path('token/refresh',
         TokenRefreshView.as_view(),
         name="token-refresh"),
    path('community/',
         views.CommunityListCreate.as_view(),
         name='community-view-create'),
    path('api-auth/',
         include("rest_framework.urls")),

]
