from rest_framework.serializers import ModelSerializer

from core.models import Carro
from core.models import Categoria
from core.models import Marca

class CarroSerializer(ModelSerializer):
    class Meta:
        model = Carro
        fields = "__all__"

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class MarcaSerializer(ModelSerializer):
    class Meta:
        model = Marca
        fields = "__all__"