# 0005: Documentação OpenAPI com drf-yasg

- **Status:** Aceito
- **Data:** 2026-11-25

## Contexto
A API navegável do DRF (ADR 0001) mostra os endpoints, mas não gera um contrato para clientes nem documenta filtros, paginação e formatos de forma centralizada.

## Opções
1. **drf-yasg:** Swagger UI + ReDoc prontos, poucas linhas de configuração. Gera OpenAPI **2.0**.
2. **drf-spectacular:** gera OpenAPI 3, é mantido mais ativamente e é a recomendação atual do DRF. Exige mais configuração.
3. **Schema nativo do DRF:** em processo de descontinuação, sem UI embutida.

## Decisão
Usar **drf-yasg 1.21** com `get_schema_view(public=True)`, servindo `/swagger/` e `/redoc/` na raiz (sem prefixo `/api/`, como o resto das rotas). Auth, permissão e throttling do schema seguem a política global (ADR 0002), sem sobrescrever.

## Consequências
- Schema gerado a partir dos ViewSets/serializers: `help_text` e docstrings viram documentação.
- O schema é público e conta no throttle (anônimo 20/dia). Cada abertura do Swagger UI gasta 2 requisições.
- OpenAPI 2.0 limita geradores de cliente modernos. Se surgir front-end/SDK, reavaliar drf-spectacular.
- Pendência: `openapi.Info` em `setup/urls.py` ainda tem valores de exemplo (contato `contact@snippets.local`, termos de serviço do Google, licença BSD). Substituir por dados reais ou remover.
