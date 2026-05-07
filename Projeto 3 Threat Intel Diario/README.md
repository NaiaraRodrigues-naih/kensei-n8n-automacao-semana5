# Projeto 3 - Threat Intel Diario com IA

Workflow n8n que toda manha as 8h le 3 RSS feeds de cyberseguranca, filtra noticias das ultimas 24h, resume com OpenAI e envia email formatado.

## Fluxo

```
Schedule 8h → RSS (x3) → Merge → Filtrar 24h → Tem noticias?
                                                      ↓ SIM
                                               OpenAI (resume + criticidade)
                                                      ↓
                                               Gmail (digest HTML)
```

| # | Node | O que faz |
|---|------|-----------|
| 1 | **Schedule Trigger** | Dispara todo dia as 8:00 |
| 2-4 | **RSS Feeds (x3)** | Le The Hacker News, Bleeping Computer, KrebsOnSecurity |
| 5-6 | **Merge (x2)** | Junta todos os artigos em uma lista unica |
| 7 | **Filtrar 24h** | Descarta artigos mais antigos que 24h; prepara prompt |
| 8 | **Tem noticias?** | Se nao ha noticias, encerra sem enviar email |
| 9 | **OpenAI** | Resume cada noticia e classifica criticidade (ALTA/MEDIA/BAIXA) |
| 10 | **Gmail** | Envia digest HTML com briefing executivo |

## Fontes monitoradas

| Feed | URL |
|------|-----|
| The Hacker News | https://feeds.feedburner.com/TheHackersNews |
| Bleeping Computer | https://www.bleepingcomputer.com/feed/ |
| KrebsOnSecurity | https://krebsonsecurity.com/feed/ |

## Como configurar no n8n

### 1. Importar
**Workflows > Import from File** → `workflow-threat-intel-diario.json`

### 2. Credencial OpenAI
No node **OpenAI Resume e classifica**, conecte sua credencial OpenAI.

### 3. Credencial Gmail
No node **Enviar email digest**, crie credencial **Gmail OAuth2**:
1. Credentials > New > Gmail OAuth2
2. Faca o login com sua conta Google e autorize o acesso

### 4. Email de destino
Adicione no arquivo `.env`:
```env
EMAIL_DESTINO=seuemail@gmail.com
```

### 5. Ativar
Toggle **Inactive → Active** — o workflow roda sozinho toda manha as 8h.

## Exemplo do email gerado

```
🛡️ Threat Intel Diario — 07/05/2026 (12 noticias)

[CRITICIDADE: ALTA] Ransomware ataca hospitais nos EUA
Resumo: Grupo LockBit 3.0 comprometeu sistemas de 5 hospitais...
Leia a noticia completa

[CRITICIDADE: MEDIA] Patch Tuesday — Microsoft corrige 78 vulnerabilidades
Resumo: A Microsoft lancou atualizacoes de seguranca para...
Leia a noticia completa

─────────────────────────────
Briefing Executivo do Dia
O cenario de ameacas desta semana e dominado por campanhas de ransomware...
```

## Variaveis de ambiente necessarias

```env
OPENAI_API_KEY=sk-proj-...        # Chave OpenAI (configurada no vault do n8n)
EMAIL_DESTINO=seuemail@gmail.com  # Quem recebe o digest
```
