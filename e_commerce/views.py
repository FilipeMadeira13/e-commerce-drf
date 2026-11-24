from django.db.models import ProtectedError
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from e_commerce.models import Categoria, Produto
from e_commerce.serializers import CategoriaSerializer, ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.order_by("id")

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "Não é possível excluir uma categoria que possui produtos."},
                status=status.HTTP_409_CONFLICT,
            )


class ProdutoViewSet(viewsets.ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.select_related("categoria").order_by("id")
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "categoria": ["exact"],
        "preco": ["gte", "lte"],
    }
    search_fields = ["nome", "categoria__nome"]
