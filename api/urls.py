# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    path(r'quizzes', views.ListQuizzes.as_view()), # quizzes endpoint
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))]