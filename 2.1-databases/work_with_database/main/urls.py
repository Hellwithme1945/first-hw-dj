from django.contrib import admin
from django.urls import path
from phones.views import show_catalog, show_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_catalog, name='catalog'),
    path('phones/<int:pk>/', show_product, name='product'),
]