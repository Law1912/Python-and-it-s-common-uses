from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('prof/', include('prof.urls')),
    path('admin/', admin.site.urls),
]