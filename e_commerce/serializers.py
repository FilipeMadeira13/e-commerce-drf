from rest_framework import serializers

from e_commerce.models import Categoria, Produto


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nome", "descricao", "criado_em", "atualizado_em"]
        extra_kwargs = {
            "criado_em": {
                "format": "%d/%m/%Y às %H:%M",
                "read_only": True,
            },
            "atualizado_em": {
                "format": "%d/%m/%Y às %H:%M",
                "read_only": True,
            },
        }


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            "id",
            "nome",
            "descricao",
            "preco",
            "quantidade_estoque",
            "categoria",
            "imagem",
            "criado_em",
            "atualizado_em",
        ]
        extra_kwargs = {
            "criado_em": {
                "format": "%d/%m/%Y às %H:%M",
                "read_only": True,
            },
            "atualizado_em": {
                "format": "%d/%m/%Y às %H:%M",
                "read_only": True,
            },
        }
