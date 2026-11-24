from django.contrib.auth.models import User
from django.core.cache import cache
from rest_framework import status
from rest_framework.test import APITestCase

from e_commerce.models import Categoria, Produto


class ExclusaoCategoriaTests(APITestCase):
    def setUp(self):
        cache.clear()  # zera contadores de throttling entre testes
        self.user = User.objects.create_user("teste", password="senha-teste-123")
        self.client.force_authenticate(self.user)
        self.categoria = Categoria.objects.create(nome="Roupas")

    def test_nao_exclui_categoria_com_produtos(self):
        Produto.objects.create(
            nome="Camiseta", preco="10.00", quantidade_estoque=1, categoria=self.categoria
        )
        resposta = self.client.delete(f"/categorias/{self.categoria.id}/")
        self.assertEqual(resposta.status_code, status.HTTP_409_CONFLICT)
        self.assertTrue(Categoria.objects.filter(id=self.categoria.id).exists())
        self.assertEqual(Produto.objects.count(), 1)

    def test_exclui_categoria_sem_produtos(self):
        resposta = self.client.delete(f"/categorias/{self.categoria.id}/")
        self.assertEqual(resposta.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Categoria.objects.filter(id=self.categoria.id).exists())
