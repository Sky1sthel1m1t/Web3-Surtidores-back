from django.urls import path, include
from rest_framework import routers

from api.viewsets import BombaViewSet, SurtidorViewSet, LoginViewSet, CombustibleViewSet, TanqueGeneralViewSet, \
    VentaViewSet

router = routers.DefaultRouter()
router.register(r'bombas', BombaViewSet)
router.register(r'combustibles', CombustibleViewSet)
router.register(r'surtidores', SurtidorViewSet)
router.register(r'tanques', TanqueGeneralViewSet)
router.register(r'ventas', VentaViewSet)
router.register('', LoginViewSet, basename='login')

urlpatterns = [
    path('', include(router.urls)),
]