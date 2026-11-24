# 0004: Comportamento ao excluir categoria

- **Status:** Aceito (implementado em `e_commerce/migrations/0003_alter_produto_categoria.py`)
- **Data:** 2026-11-24

## Contexto
`Produto.categoria` usa `on_delete=models.CASCADE`: um `DELETE /categorias/{id}/` remove silenciosamente todos os produtos da categoria. Não há registro de que isso tenha sido intencional.

## Opções
1. **CASCADE (atual):** simples, mas há risco de perda de dados por um único request.
2. **PROTECT:** impede excluir categoria com produtos (`ProtectedError`, que precisa virar HTTP 409/400 na view). Mais seguro.
3. **SET_NULL:** produtos ficam sem categoria. Exige `null=True` e migration, e contraria `categoria` ser obrigatória.

## Decisão
Usar **`on_delete=models.PROTECT`** em `Produto.categoria`. O catálogo não deve perder produtos como efeito colateral da exclusão de uma categoria.

## Consequências
- Para excluir uma categoria, antes é preciso excluir os produtos dela ou movê-los para outra categoria.
- Implementação: alterar o model, gerar migration e tratar `ProtectedError` no `CategoriaViewSet` (responder HTTP 409 com mensagem clara em vez de erro 500). Depois, atualizar o aviso no README e o CHANGELOG.
