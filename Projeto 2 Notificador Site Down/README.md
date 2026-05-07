# Projeto 2 - Notificador de Site Down

Workflow n8n que monitora um site a cada 5 minutos e envia alerta no Telegram quando ele cai ou volta ao ar.

## O que ele faz

```
Schedule (5min) → HTTP Request → Verificar Estado → Switch
                                                      ├─ Site caiu    → Telegram 🚨
                                                      ├─ Site voltou  → Telegram ✅
                                                      └─ Sem mudanca  → (nada)
```

| # | Node | O que faz |
|---|------|-----------|
| 1 | **Schedule Trigger** | Dispara automaticamente a cada 5 minutos |
| 2 | **Checar site** | Faz GET na URL; nao quebra se o site nao responder |
| 3 | **Verificar estado** | Compara status atual com o anterior (salvo em memoria) |
| 4 | **O que mudou?** | Roteia: caiu / voltou / sem mudanca |
| 5 | **Alerta Site Caiu** | Telegram com horario e codigo de erro |
| 6 | **Aviso Site Voltou** | Telegram confirmando que voltou ao ar |

## Cenarios cobertos

- Site retorna 200 (normal) → nenhuma acao
- Site cai (4xx, 5xx, timeout) → alerta de queda enviado UMA vez
- Site volta ao ar → aviso de retorno enviado UMA vez
- Sem mudanca de estado → silencio (sem spam)

## Como configurar no n8n

### 1. Importar
**Workflows > Import from File** → selecione `workflow-notificador-site-down.json`

### 2. Credencial do Telegram
1. No Telegram, abra **@BotFather** e envie `/newbot`
2. Copie o token gerado
3. No n8n: **Credentials > New > Telegram API** → cole o token
4. Descubra seu Chat ID acessando:
   `https://api.telegram.org/bot<TOKEN>/getUpdates`

### 3. Ativar
Clique no toggle **Inactive → Active** — o workflow roda sozinho a cada 5 minutos.

## Mensagens enviadas

**Queda:**
```
🚨 ALERTA: Site fora do ar!
🌐 URL: https://naiararodrigues-naih.github.io/...
⏰ Horario: 07/05/2026 14:35:00
📊 Status: 503
⚠️ Verifique imediatamente!
```

**Retorno:**
```
✅ Site voltou ao ar!
🌐 URL: https://naiararodrigues-naih.github.io/...
⏰ Horario: 07/05/2026 14:40:00
📊 Status: 200 OK
✨ Tudo funcionando normalmente.
```
