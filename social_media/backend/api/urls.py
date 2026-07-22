from django.urls import path
from . import views
urlpatterns = [
    path('tweets/', views.create_tweets),
    path('profiles/', views.create_profile),
]
