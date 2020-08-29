from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Paths for Django
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),

    # Paths for React
    path('', include('frontend.urls')),

    # Paths for API
    path('api/mascots/', include('mascots.urls')),
    path('api/teams/', include('teams.urls'))
]

if settings.DEBUG:
  import debug_toolbar
  urlpatterns = [
      path('__debug__/', include(debug_toolbar.urls)),
  ] + urlpatterns
