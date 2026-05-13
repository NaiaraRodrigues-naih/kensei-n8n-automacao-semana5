# Monitor de Email Vazado

Verifica se um email apareceu em vazamentos de dados usando a API HaveIBeenPwned. Envia alerta no Telegram com detalhes dos vazamentos encontrados.

## Fluxo

```
POST /webhook/check-email
        ↓
   HaveIBeenPwned API
        ↓
   Email foi vazado?
   ↙              ↘
SIM                NÃO
↓                   ↓
Formatar Alerta    Formatar OK
↓                   ↓
Telegram 🚨        Telegram ✅
↓                   ↓
Resposta JSON      Resposta JSON
```

## Exemplo de resposta

**Email vazado:**
```json
{ "email": "teste@gmail.com", "vazado": true, "total_vazamentos": 3, "alerta_enviado": true }
```

**Email seguro:**
```json
{ "email": "teste@gmail.com", "vazado": false, "total_vazamentos": 0, "alerta_enviado": false }
```

## Mensagem no Telegram (quando vazado)

```
🚨 ALERTA DE VAZAMENTO!

O email teste@gmail.com foi encontrado em 3 vazamento(s):

1. Adobe (2013)
   Contas afetadas: 152.445.165
   Dados expostos: Email, Password, Username

2. LinkedIn (2012)
   Contas afetadas: 164.611.595
   Dados expostos: Email, Password

⚠️ Recomendacao: troque suas senhas imediatamente e ative autenticacao em dois fatores.
```

## Configuração

### 1. API Key do HaveIBeenPwned

A API v3 requer uma chave paga (~USD 3,50/mês): haveibeenpwned.com/API/Key

Adicione no `.env`:
```
HIBP_API_KEY=SUA_CHAVE_HIBP_AQUI
```

### 2. Telegram

Use as credenciais do Projeto 2 (já configuradas no n8n).

Adicione no `.env` se ainda não tiver:
```
TELEGRAM_BOT_TOKEN=SEU_TOKEN
TELEGRAM_CHAT_ID=SEU_CHAT_ID
```

### 3. Importar no n8n

1. n8n → Workflows → Import from File
2. Selecione `workflow-monitor-email-vazado.json`
3. Configure as credenciais do Telegram no node
4. Ative o workflow

## Como usar

```bash
curl -X POST https://naiararodriguespro.app.n8n.cloud/webhook/check-email \
  -H "Content-Type: application/json" \
  -d '{"email":"seuemail@gmail.com"}'
```
