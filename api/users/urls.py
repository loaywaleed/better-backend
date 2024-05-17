from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('users/signup/',
         views.UserCreate.as_view(),
         name="user-create"),
    path('token/',
         TokenObtainPairView.as_view(),
         name="token-view"),
    path('token/refresh',
         TokenRefreshView.as_view(),
         name="token-refresh"),
    path('user/',
         views.UserView.as_view(), name="user-home-view"),
    path('api-auth/',
         include("rest_framework.urls")),
]
