# Changelog

Todas as mudanças relevantes deste projeto são registradas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Added
- Documentação interativa da API com drf-yasg: Swagger UI em `/swagger/` e ReDoc em `/redoc/` (ADR 0005, `f5c9c00`).
- Projeto Django (`setup/`) e app `e_commerce` com os models `Categoria` e `Produto`. `SECRET_KEY` lida do `.env` (`bcd847e`).
- API REST com CRUD de categorias (`/categorias/`) e produtos (`/produtos/`) via DRF (`94508ce`).
- Filtros de produtos por `categoria` e faixa de preço (`preco__gte`, `preco__lte`), busca por nome do produto/categoria (`search`) e permissão padrão `IsAuthenticatedOrReadOnly` (`c4b64b8`).
- Paginação de 20 itens por página (`8f3ee53`).
- Throttling: 20 requisições/dia para anônimos e 50/dia para autenticados (`2ee567d`).
- Testes de exclusão de categoria (`e_commerce/tests.py`) (`0d84a8c`).
- Documentação: README, CLAUDE.md, CHANGELOG e ADRs 0001–0004 em `docs/decisoes/` (`64f891b`).

### Changed
- Migrations iniciais unificadas (`b2f2819`).
- Localização: `LANGUAGE_CODE` de `en-us` para `pt-br` e `TIME_ZONE` de `UTC` para `America/Fortaleza` (`64f891b`).
- **Breaking:** `Produto.categoria` passa de `CASCADE` para `PROTECT`. `DELETE /categorias/{id}/` em uma categoria com produtos agora retorna `409 Conflict` em vez de apagar os produtos (ADR 0004, `0d84a8c`).
