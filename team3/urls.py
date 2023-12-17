
from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('check/', include('check.urls')),
    path('', include('home.urls')),
    path('two/', include('two.urls')),
]

