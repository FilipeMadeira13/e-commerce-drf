from rest_framework import filters, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from e_commerce.models import Categoria, Produto
from e_commerce.serializers import CategoriaSerializer, ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()


class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.select_related("categoria")
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "categoria": ["exact"],
        "preco": ["gte", "lte"],
    }
    search_fields = ["nome", "categoria__nome"]
