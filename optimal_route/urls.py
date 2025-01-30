from django.contrib import admin
from django.urls import include, path

from route.urls import url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('route/', include(url_patterns)),
]
