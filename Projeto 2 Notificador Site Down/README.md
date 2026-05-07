# Projeto 2 - Notificador de Site Down

Workflow n8n que monitora um site a cada 5 minutos e envia alerta no Telegram se ele cair.

## O que ele faz

```
Schedule (5min) → HTTP Request → IF status == 200 → [nada]
                                        ↓ nao
                                  Alerta no Telegram
```

| # | Node | O que faz |
|---|------|-----------|
| 1 | **Schedule Trigger** | Dispara automaticamente a cada 5 minutos |
| 2 | **Checar site** | Faz GET na URL; nao quebra se o site nao responder |
| 3 | **Site esta no ar?** | Verdadeiro se statusCode == 200; falso = site caiu |
| 4 | **Alerta no Telegram** | Envia mensagem formatada com horario e status do erro |

## Cenarios cobertos

- Site retorna 200 → nenhuma acao (branch verdadeiro vazio)
- Site retorna 4xx ou 5xx → alerta enviado com o codigo de status
- Site nao responde (timeout, DNS, conexao recusada) → alerta enviado com "Sem resposta"

## Como configurar

### 1. Importar no n8n

1. **Workflows > Import from File** → selecione `workflow-notificador-site-down.json`

### 2. Credencial do Telegram

Voce precisa de um bot do Telegram. Siga os passos:

1. No Telegram, abra **@BotFather** e envie `/newbot`
2. Siga as instrucoes e copie o **token** gerado (ex: `123456:ABC-DEF...`)
3. No n8n, vá em **Credentials > New > Telegram API** e cole o token
4. Para descobrir seu **Chat ID**:
   - Envie qualquer mensagem para o seu bot
   - Acesse: `https://api.telegram.org/bot<SEU_TOKEN>/getUpdates`
   - O `chat.id` aparece no JSON de resposta

### 3. Configurar variaveis de ambiente

Adicione no arquivo `.env` (nunca commite esse arquivo):

```env
TELEGRAM_CHAT_ID=seu_chat_id_aqui
```

No node **Alerta no Telegram**, o Chat ID ja usa `{{ $env.TELEGRAM_CHAT_ID }}`.

### 4. Ativar o workflow

- Conecte a credencial do Telegram no node **Alerta no Telegram**
- Clique no toggle **Active** no canto superior direito
- O workflow passa a rodar automaticamente a cada 5 minutos

## Mensagem de alerta (exemplo)

```
🚨 ALERTA: Site fora do ar!

🌐 URL: https://naiararodrigues-naih.github.io/...
⏰ Horario: 07/05/2026 14:35:00
📊 Status: 503

⚠️ Verifique imediatamente!
```
