from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Posts ),
    path('delete', views.delete, name = 'delete')
]