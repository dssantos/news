from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news_api import views


router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('news', views.NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]
