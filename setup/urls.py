from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from credit_card_management.views import CategoryViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
