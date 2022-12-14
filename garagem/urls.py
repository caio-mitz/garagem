from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CarroViewSet
from core.views import CategoriaViewSet
from core.views import MarcaViewSet

router = DefaultRouter()
router.register(r'carros', CarroViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'marcas', MarcaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]