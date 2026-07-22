from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.urls import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('tweet/', include('tweet.urls')),
=======
>>>>>>> cf35ad6f5963e5493405be934416769a15ded7a0
    path('', include('tweet.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
