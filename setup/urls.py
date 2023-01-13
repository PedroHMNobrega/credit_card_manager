from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from credit_card_management.views import CategoryViewSet, PurchaseViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('purchases', PurchaseViewSet, basename='purchases')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
