from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('shop.urls', namespace='shop')),
    path('admin/', admin.site.urls),
]
