from django.contrib import admin
from django.urls import path
from phones.views import show_catalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', show_catalog),
]
