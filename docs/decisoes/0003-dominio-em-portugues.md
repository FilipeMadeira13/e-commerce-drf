# 0003: Domínio em português e formato de datas

- **Status:** Aceito
- **Data:** 2026-11-21 (registrado retroativamente em 2026-11-24)

## Contexto
O público e a equipe são brasileiros. Era preciso padronizar a nomenclatura do domínio e a apresentação de datas na API.

## Decisão
- Models, campos e rotas em português (`Categoria`, `Produto`, `preco`, `quantidade_estoque`, `criado_em`, `/produtos/`).
- Campos `criado_em`/`atualizado_em` são `read_only` e serializados como `"%d/%m/%Y às %H:%M"`.

## Consequências
- Código de framework (Django/DRF) continua em inglês, então o código fica misto.
- Localização alinhada ao domínio: `LANGUAGE_CODE = "pt-br"` e `TIME_ZONE = "America/Fortaleza"`. Mensagens de erro do Django/DRF saem em português e as datas no horário local.
- O formato não é ISO 8601, o que dificulta o parsing por clientes. Se surgir um front-end, considerar ISO na API e formatar no cliente.
