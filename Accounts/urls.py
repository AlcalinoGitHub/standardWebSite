from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register ),
    path('login/', views.login),
    path('logout/', views.logout )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)