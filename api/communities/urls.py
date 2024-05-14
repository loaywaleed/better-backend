from django.urls import path
from . import views


urlpatterns = [
    path('',
         views.CommunityListCreate.as_view(),
         name='community-view-create'),
]