# 0002: Política padrão da API

- **Status:** Aceito
- **Data:** 2026-11-23 / 2026-11-24 (registrado retroativamente em 2026-11-24)

## Contexto
O catálogo deve ser público para leitura, mas protegido para escrita, e a API não deve ficar exposta a uso abusivo.

## Decisão
Configurar globalmente em `REST_FRAMEWORK` (`setup/settings.py`), sem sobrescrever por view:
- **Autenticação:** `SessionAuthentication` + `BasicAuthentication`.
- **Permissão:** `IsAuthenticatedOrReadOnly`.
- **Paginação:** `PageNumberPagination`, `PAGE_SIZE = 20`.
- **Throttling:** `AnonRateThrottle` 20/dia, `UserRateThrottle` 50/dia.

## Consequências
- Comportamento uniforme em todos os endpoints; exceções exigem novo ADR.
- Querysets precisam de `order_by` para paginação consistente.
- Os limites de throttling são baixos: esgotam rápido em desenvolvimento e são restritivos para um e-commerce real. Revisar antes de produção.
- Basic auth envia credenciais a cada requisição: exige HTTPS fora de dev. Auth por token/JWT pode ser necessária para clientes front-end/mobile.
