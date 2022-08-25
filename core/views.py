from rest_framework.viewsets import ModelViewSet

from core.models import Carro
from core.models import Categoria
from core.models import Marca
from core.serializers import CarroSerializer
from core.serializers import CategoriaSerializer
from core.serializers import MarcaSerializer

class CarroViewSet(ModelViewSet):
    queryset = Carro.objects.all()
    serializer_class = CarroSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
