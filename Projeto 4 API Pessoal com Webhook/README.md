# Projeto 4 - API Pessoal com Webhook

Mini-API de análise de sentimentos construída com n8n + OpenAI. Sem servidor. Sem deploy. Funciona como uma API real.

## Fluxo

```
POST /webhook/sentiment
        ↓
   Webhook (n8n)
        ↓
   OpenAI gpt-4o-mini
        ↓
   Formatar Resposta (Code node)
        ↓
   Respond JSON
```

## Como importar o workflow

1. Abra o n8n
2. Clique em **Workflows → Import from File**
3. Selecione `workflow_projeto4.json`
4. Configure sua credencial da OpenAI no node **OpenAI - Analisar Sentimento**
5. Clique em **Activate** para ativar o webhook

## Como usar a API

### Endpoint

```
POST https://SEU-N8N/webhook/sentiment
Content-Type: application/json
```

### Body da requisição

```json
{
  "texto": "Adorei o curso da Kensei! O conteúdo é incrível."
}
```

### Resposta

```json
{
  "sentimento": "positivo",
  "confianca": 0.97,
  "palavras_chave": ["curso", "Kensei", "conteúdo", "incrível", "adorei"]
}
```

Valores possíveis para `sentimento`: `positivo`, `negativo`, `neutro`

### Exemplo com curl

```bash
curl -X POST http://localhost:5678/webhook/sentiment \
  -H "Content-Type: application/json" \
  -d '{"texto":"Adorei o curso da Kensei!"}'
```

## Testar com Python

```bash
pip install requests
python testar_api.py
```

O script executa 4 casos de teste automáticos e permite digitar um texto customizado.

## Arquivos

| Arquivo | Descrição |
|---|---|
| `workflow_projeto4.json` | Workflow para importar no n8n |
| `testar_api.py` | Script Python para testar a API |
| `README.md` | Esta documentação |

## Desafio extra implementado

O campo `palavras_chave` retorna de 3 a 5 palavras mais relevantes do texto analisado, conforme o desafio extra da aula.
