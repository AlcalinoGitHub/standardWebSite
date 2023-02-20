from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.MainPage ),
    path('like/', views.LikePost, name = 'like'),
    path('comment/', views.comment, name = 'comment'),
    path('delete_comment', views.delete_comment, name = 'delete_comment')
]