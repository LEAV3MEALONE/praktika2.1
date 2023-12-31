from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.RegisterView.as_view(), name='register')
]
