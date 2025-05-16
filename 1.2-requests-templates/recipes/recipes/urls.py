from django.contrib import admin
from django.urls import path
from calculator.views import recipe_view

urlpatterns = [
    path('<str:dish>/', recipe_view),
    path('admin/', admin.site.urls),
]
