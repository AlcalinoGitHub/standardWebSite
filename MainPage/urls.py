from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MainPage ),
    path('like/', views.LikePost, name = 'like')
]