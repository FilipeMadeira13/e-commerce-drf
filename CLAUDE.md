# CLAUDE.md

## Comandos
```bash
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
python manage.py test
python manage.py makemigrations   # após qualquer mudança em models
```
Requer `.env` na raiz com `DJANGO_SECRET_KEY` (sem ele o settings quebra com `KeyError`).

## Arquitetura
- `setup/`: projeto Django (settings, urls). Rotas via `DefaultRouter` na raiz, **sem prefixo `/api/`**.
- `e_commerce/`: app único. Fluxo `models.py` → `serializers.py` (ModelSerializer) → `views.py` (ModelViewSet).
- Política da API (auth, permissão, paginação, throttling) é **global** em `REST_FRAMEWORK` no settings. Ver [docs/decisoes/](docs/decisoes/).
- Banco: SQLite (`db.sqlite3`).

## Convenções
- Nomes de domínio, campos e rotas em português (`Categoria`, `preco`, `/produtos/`).
- `criado_em`/`atualizado_em`: `read_only`, formato `"%d/%m/%Y às %H:%M"` no serializer.
- Querysets de ViewSet sempre com `order_by(...)` (a paginação exige ordem) e `select_related` em FKs.
- Commits: Conventional Commits em pt-BR (`feat:`, `refactor:`, `chore:`).
- Registrar mudanças no `CHANGELOG.md` e decisões novas como ADR em `docs/decisoes/`.

## Regras
- Nunca commitar `.env` nem `db.sqlite3`.
- Throttle global: anônimo 20/dia, autenticado 50/dia. Testes manuais esgotam isso rápido.
- Não sobrescrever auth/permissão/paginação por view sem registrar um ADR.
