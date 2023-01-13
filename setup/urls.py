from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from credit_card_management.views import CategoryViewSet, PurchaseViewSet, InstallmentViewSet

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('purchases', PurchaseViewSet, basename='purchases')
router.register('installments', InstallmentViewSet, basename='installments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
