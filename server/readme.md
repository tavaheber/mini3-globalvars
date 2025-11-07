# API de Variáveis Globais

Esta API permite criar, ler, atualizar e remover variáveis globais usando endpoints REST simples.

## Endpoints

| Método | Endpoint | Descrição |
|-------|---------|-----------|
| `GET` | `/` | Lista todos os nomes de variáveis globais disponíveis. |
| `GET` | `/<var_name>` | Recupera o valor de uma variável global com o nome especificado. |
| `POST` | `/<var_name>` | Cria ou atualiza uma variável global. O corpo da requisição deve conter o novo valor. |
| `DELETE` | `/<var_name>` | Remove uma variável global com o nome especificado. |

## Restrições
- Os nomes das variáveis devem conter **apenas letras** (a-z, A-Z). Caracteres especiais ou números são proibidos.
- A API usa um banco de dados em memória (`:memory:`), portanto, os dados são perdidos ao encerrar o servidor.