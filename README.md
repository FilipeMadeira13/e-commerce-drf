# E-commerce: API de catálogo

API REST em Django + Django REST Framework para gerenciar **categorias** e **produtos**.

## Requisitos
- Python 3.13
- Dependências em [requirements.txt](requirements.txt) (Django 6.1, DRF 3.18, django-filter, drf-yasg, python-dotenv)

## Instalação
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo 'DJANGO_SECRET_KEY=troque-esta-chave' > .env

python manage.py migrate
python manage.py createsuperuser   # necessário para escrever na API
python manage.py runserver
```

## Endpoints

| Rota | Métodos | Descrição |
|---|---|---|
| `/` | GET | Raiz navegável do DRF |
| `/categorias/` | GET, POST | Lista / cria categorias |
| `/categorias/{id}/` | GET, PUT, PATCH, DELETE | Detalhe de categoria |
| `/produtos/` | GET, POST | Lista / cria produtos |
| `/produtos/{id}/` | GET, PUT, PATCH, DELETE | Detalhe de produto |
| `/swagger/` | GET | Documentação interativa (Swagger UI). Schema JSON em `/swagger/?format=openapi` |
| `/redoc/` | GET | Documentação da API (ReDoc) |
| `/admin/` | - | Django Admin (models ainda não registrados) |

> Uma categoria que possui produtos **não pode ser excluída**: a API responde `409 Conflict`. Exclua os produtos ou mova-os para outra categoria antes. Ver [ADR 0004](docs/decisoes/0004-exclusao-categoria-cascade.md).

### Filtros e busca (`/produtos/`)
| Parâmetro | Exemplo |
|---|---|
| `categoria` | `?categoria=1` |
| `preco__gte` / `preco__lte` | `?preco__gte=10&preco__lte=100` |
| `search` (nome do produto ou da categoria) | `?search=camiseta` |
| `page` | `?page=2` |

```bash
curl "http://127.0.0.1:8000/produtos/?categoria=1&preco__lte=100&search=camiseta"
curl -u admin:senha -X POST http://127.0.0.1:8000/categorias/ \
     -H "Content-Type: application/json" -d '{"nome": "Roupas"}'
```

## Regras da API
- **Autenticação:** Session ou HTTP Basic.
- **Permissão:** leitura pública; criar, editar e excluir exigem login.
- **Paginação:** 20 itens por página (`count`, `next`, `previous`, `results`).
- **Limite de requisições:** anônimo 20/dia, autenticado 50/dia (HTTP 429 ao exceder). Vale também para `/swagger/` e `/redoc/`.
- **Datas:** `criado_em`/`atualizado_em` no formato `dd/mm/aaaa às HH:MM` (horário `America/Fortaleza`).

## Testes
```bash
python manage.py test
```

## Documentação
- Documentação interativa da API: `/swagger/` e `/redoc/` (com o servidor rodando)
- [CHANGELOG.md](CHANGELOG.md)
- [Decisões de arquitetura (ADRs)](docs/decisoes/)
