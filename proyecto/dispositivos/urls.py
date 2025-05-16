from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DispositivoViewSet

router = DefaultRouter()
router.register(r'', DispositivoViewSet, basename='dispositivo')

urlpatterns = [
    path('', include(router.urls)),
]