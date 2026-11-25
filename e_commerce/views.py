from django.db.models import ProtectedError
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from e_commerce.models import Categoria, Produto
from e_commerce.serializers import CategoriaSerializer, ProdutoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    """
    CRUD de categorias de produtos, exposto em `/categorias/`.

    Leitura é pública; escrita exige autenticação. Paginação, permissão e
    throttling seguem a política global definida em `REST_FRAMEWORK`.

    list:
    Lista as categorias.

    Resultado paginado (20 itens por página), ordenado por `id`.

    retrieve:
    Retorna uma categoria.

    Responde `404 Not Found` se o `id` não existir.

    create:
    Cria uma categoria.

    Requer autenticação.

    update:
    Substitui todos os campos de uma categoria.

    Requer autenticação.

    partial_update:
    Atualiza parcialmente uma categoria.

    Apenas os campos enviados são alterados. Requer autenticação.
    """

    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.order_by("id")

    def destroy(self, request, *args, **kwargs):
        """
        Exclui uma categoria.

        Requer autenticação. Como `Produto.categoria` usa `on_delete=PROTECT`,
        categorias com produtos vinculados não podem ser excluídas: nesse caso a
        API responde `409 Conflict` em vez de `204 No Content` (ver ADR 0004).
        """
        try:
            return super().destroy(request, *args, **kwargs)
        except ProtectedError:
            return Response(
                {"detail": "Não é possível excluir uma categoria que possui produtos."},
                status=status.HTTP_409_CONFLICT,
            )


class ProdutoViewSet(viewsets.ModelViewSet):
    """
    CRUD de produtos do catálogo, exposto em `/produtos/`.

    Leitura é pública; escrita exige autenticação. Paginação, permissão e
    throttling seguem a política global definida em `REST_FRAMEWORK`.

    list:
    Lista os produtos, com filtros e busca.

    Resultado paginado (20 itens por página), ordenado por `id`.

    Parâmetros de query:

    - `categoria`: `id` exato da categoria.
    - `preco__gte` / `preco__lte`: faixa de preço (inclusiva).
    - `search`: busca textual no nome do produto e no nome da categoria.

    retrieve:
    Retorna um produto.

    Responde `404 Not Found` se o `id` não existir.

    create:
    Cria um produto.

    Requer autenticação. `preco` deve ser maior ou igual a 0,01 e `categoria`
    deve referenciar uma categoria existente.

    update:
    Substitui todos os campos de um produto.

    Requer autenticação.

    partial_update:
    Atualiza parcialmente um produto.

    Apenas os campos enviados são alterados. Requer autenticação.

    destroy:
    Exclui um produto.

    Requer autenticação.
    """

    serializer_class = ProdutoSerializer
    queryset = Produto.objects.select_related("categoria").order_by("id")
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = {
        "categoria": ["exact"],
        "preco": ["gte", "lte"],
    }
    search_fields = ["nome", "categoria__nome"]
