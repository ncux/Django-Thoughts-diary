
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('thoughts.urls', namespace='thoughts')),
    path('admin/', admin.site.urls),
]
