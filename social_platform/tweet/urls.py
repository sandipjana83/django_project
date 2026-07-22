from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.tweet_list,name='tweet_list' ),
    path('create/',views.tweet_create,name='tweet_create'),
    path('<int:tweet_id>/edit/',views.tweet_edit,name='tweet_edit'),
    path('<int:tweet_id>/delete/',views.tweet_del,name='tweet_del'),
    path('register/', views.register, name='register'),
    path("logout/", views.logged_out, name="logged_out"),
    path("profile/", views.profile, name="profile"),
    path("resetPass/", views.sent_email, name="sent_email"),
]