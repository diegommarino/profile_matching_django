from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('profile_matching.profiles.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
]
