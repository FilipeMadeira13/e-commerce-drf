# 0001: Stack Django + DRF + django-filter

- **Status:** Aceito
- **Data:** 2026-11-21 (registrado retroativamente em 2026-11-24)

## Contexto
O projeto precisa de uma API REST para o catálogo (categorias e produtos), com CRUD, filtros e admin.

## Decisão
- Django 6.1 como framework, com projeto `setup/` e um único app `e_commerce/`.
- Django REST Framework 3.18 com `ModelSerializer` + `ModelViewSet` + `DefaultRouter`.
- django-filter para filtros declarativos (`filterset_fields`).
- python-dotenv para ler segredos de `.env` (`DJANGO_SECRET_KEY` obrigatório).
- SQLite como banco em desenvolvimento.

## Consequências
- CRUD completo com pouco código; a API navegável do DRF serve como documentação mínima.
- `DEBUG=True` e `ALLOWED_HOSTS=[]` estão fixos no settings: antes de produção será preciso parametrizar via `.env` e trocar o banco.
