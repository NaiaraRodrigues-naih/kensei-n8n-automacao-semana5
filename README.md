# Trilha Kensei Cybersecurity — Python & Automação com n8n (Semana 5)

> **Aluna:** Naiara Rodrigues  
> **Trilha:** Automação com Python e n8n  
> **Semana:** 5 — Workflows de Automação aplicados a Cybersecurity  
> **Repositório:** [github.com/NaiaraRodrigues-naih/kensei-n8n-automacao-semana5](https://github.com/NaiaraRodrigues-naih/kensei-n8n-automacao-semana5)

---

## Sumário

1. [Sobre a Trilha](#sobre-a-trilha)
2. [O que é o n8n?](#o-que-é-o-n8n)
3. [Estrutura do Repositório](#estrutura-do-repositório)
4. [Projeto 1 — Gerador de Frases Motivacionais com OpenAI e Google Sheets](#projeto-1--gerador-de-frases-motivacionais-com-openai-e-google-sheets)
5. [Projeto 2 — Notificador de Site Down via Telegram](#projeto-2--notificador-de-site-down-via-telegram)
6. [Projeto 3 — Threat Intel Diário com IA e Email Digest](#projeto-3--threat-intel-diário-com-ia-e-email-digest)
7. [Configuração Geral do Ambiente](#configuração-geral-do-ambiente)
8. [Perguntas e Respostas sobre os Projetos](#perguntas-e-respostas-sobre-os-projetos)
9. [Aprendizados da Semana](#aprendizados-da-semana)

---

## Sobre a Trilha

A **Trilha Kensei Cybersecurity** é um programa de capacitação em segurança da informação que combina fundamentos de Python com ferramentas modernas de automação. Na **Semana 5**, o foco foi em **automação de workflows** usando o n8n — uma ferramenta open-source de orquestração de tarefas — integrado a serviços como OpenAI, Google Sheets, Telegram e Gmail.

O objetivo da semana foi demonstrar como a automação pode ser aplicada diretamente em cenários reais de cybersecurity: desde a geração de conteúdo até o monitoramento de infraestrutura e coleta de inteligência sobre ameaças.

---

## O que é o n8n?

O **n8n** (pronuncia-se "n-eight-n") é uma plataforma de automação de workflows **low-code / no-code** e **open-source**. Ele funciona como um "canivete suíço de integrações": conecta APIs, bancos de dados, serviços em nuvem e muito mais, sem precisar escrever centenas de linhas de código.

### Conceitos fundamentais do n8n

| Conceito | O que é |
|----------|---------|
| **Workflow** | Sequência de tarefas automatizadas conectadas entre si |
| **Node** | Bloco individual que executa uma ação (ex: chamar uma API, filtrar dados) |
| **Trigger** | Node inicial que dispara o workflow (manual, agendado, webhook, etc.) |
| **Credencial** | Chave de acesso salva de forma segura para autenticar APIs externas |
| **Execution** | Uma execução completa do workflow do início ao fim |

### Por que usar o n8n em Cybersecurity?

- **Monitoramento contínuo** sem depender de scripts manuais
- **Alertas em tempo real** via Telegram, Slack, e-mail, etc.
- **Coleta e análise de Threat Intelligence** de forma automatizada
- **Integração com ferramentas de segurança** (SIEM, feeds de IOCs, scanners)
- **Resposta a incidentes** automatizada para ações repetitivas

---

## Estrutura do Repositório

```
kensei-n8n-automacao-semana5/
│
├── Projeto 1 Seu Primeiro Workflow/
│   ├── README.md                                              # Documentação do Projeto 1
│   └── workflow-frase-motivacional-openai-google-sheets.json # Workflow exportado
│
├── Projeto 2 Notificador Site Down/
│   ├── README.md                                             # Documentação do Projeto 2
│   └── workflow-notificador-site-down.json                   # Workflow exportado
│
├── Projeto 3 Threat Intel Diario/
│   ├── README.md                                             # Documentação do Projeto 3
│   └── workflow-threat-intel-diario.json                     # Workflow exportado
│
├── .env.example    # Modelo de variáveis de ambiente (sem dados reais)
├── .gitignore      # Arquivos que NÃO devem ir para o GitHub (ex: .env com chaves)
└── README.md       # Este arquivo — visão geral de toda a semana
```

> **Importante sobre segurança:** O arquivo `.env` com as chaves reais **nunca é enviado para o GitHub**. Apenas o `.env.example` (com valores fictícios) fica no repositório. Isso é uma boa prática de segurança para não expor credenciais publicamente.

---

## Projeto 1 — Gerador de Frases Motivacionais com OpenAI e Google Sheets

### O que o projeto faz

Ao clicar em **Manual Trigger** no n8n, o workflow:
1. Solicita à **OpenAI (GPT)** a geração de uma frase motivacional curta em português
2. Organiza os campos: `data`, `frase` e `fonte`
3. Adiciona automaticamente uma nova linha em uma **planilha do Google Sheets**

### Diagrama do fluxo

```
Manual Trigger → OpenAI (gera frase) → Set (formata campos) → Google Sheets (salva)
```

### Nodes utilizados

| # | Node | Função |
|---|------|--------|
| 1 | **Manual Trigger** | Dispara o workflow ao clicar em "Execute" |
| 2 | **OpenAI - Chat Model** | Envia prompt para o GPT e recebe a frase gerada |
| 3 | **Set** | Organiza os dados: data atual, frase recebida e nome da fonte |
| 4 | **Google Sheets** | Insere uma nova linha na aba `Frases` da planilha |

### Passo a passo para importar e usar

**1. Importar o workflow**
- Abra o n8n
- Vá em **Workflows > Import from File**
- Selecione o arquivo `workflow-frase-motivacional-openai-google-sheets.json`

**2. Configurar credencial da OpenAI**
- No node **Gerar frase com OpenAI**, clique em "Credential"
- Selecione ou crie uma credencial do tipo **OpenAI API**
- Cole sua `OPENAI_API_KEY`

**3. Configurar credencial do Google Sheets**
- No node **Salvar no Google Sheets**, clique em "Credential"
- Crie uma credencial do tipo **Google Sheets OAuth2**
- Faça login com sua conta Google e autorize o acesso

**4. Preparar a planilha**
- Crie uma aba chamada `Frases` na planilha
- Adicione as colunas: `data | frase | fonte`

**5. Executar**
- Clique no botão **Execute Workflow** (Manual Trigger)
- Verifique a planilha — uma nova linha deve aparecer!

### Por que este projeto é relevante para cybersecurity?

Este projeto demonstra o conceito de **integração entre IA e ferramentas de produtividade**, base para cenários mais avançados como geração automatizada de relatórios de segurança, logs de incidentes, ou resumos de vulnerabilidades salvos em planilhas.

---

## Projeto 2 — Notificador de Site Down via Telegram

### O que o projeto faz

Um workflow que **monitora um site a cada 5 minutos** e envia alertas no **Telegram** quando ele cai ou volta ao ar — sem spam, apenas uma notificação por evento.

### Diagrama do fluxo

```
Schedule (5min) → HTTP Request → Verificar Estado → Switch
                                                     ├─ Site caiu    → Telegram 🚨
                                                     ├─ Site voltou  → Telegram ✅
                                                     └─ Sem mudança  → (nada)
```

### Nodes utilizados

| # | Node | Função |
|---|------|--------|
| 1 | **Schedule Trigger** | Dispara automaticamente a cada 5 minutos (cron) |
| 2 | **HTTP Request** | Faz GET na URL alvo; não quebra o fluxo se o site não responder |
| 3 | **Code / Function** | Compara o status atual com o anterior (salvo em memória) |
| 4 | **Switch** | Roteia: site caiu / site voltou / sem mudança |
| 5 | **Telegram (alerta queda)** | Envia mensagem com horário e código de erro |
| 6 | **Telegram (aviso retorno)** | Envia mensagem confirmando que voltou ao ar |

### Lógica de estado (anti-spam)

O sistema **guarda o estado anterior** do site (online/offline). Só envia notificação quando o estado **muda**:

- Site estava **online** → ficou **offline** → envia alerta 🚨
- Site estava **offline** → voltou **online** → envia aviso ✅
- Estado não mudou → **silêncio** (sem mensagens repetidas)

Isso evita que você receba dezenas de mensagens iguais a cada 5 minutos durante uma queda prolongada.

### Cenários cobertos

| Situação | Ação do workflow |
|----------|-----------------|
| Site retorna 200 (normal) | Nenhuma ação |
| Site cai (4xx, 5xx, timeout) | Alerta de queda enviado **uma vez** |
| Site volta ao ar | Aviso de retorno enviado **uma vez** |
| Sem mudança de estado | Silêncio (sem spam) |

### Passo a passo para configurar

**1. Importar o workflow**
- **Workflows > Import from File** → selecione `workflow-notificador-site-down.json`

**2. Criar um bot no Telegram**
- Abra o Telegram e busque **@BotFather**
- Envie o comando `/newbot` e siga as instruções
- Copie o **token** gerado (ex: `123456:ABC-xyz...`)

**3. Descobrir seu Chat ID**
- Acesse no navegador:  
  `https://api.telegram.org/bot<SEU_TOKEN>/getUpdates`
- Envie qualquer mensagem para o bot e recarregue a página
- Procure o campo `"chat": {"id": XXXXXXX}` — esse é o seu Chat ID

**4. Configurar credencial no n8n**
- **Credentials > New > Telegram API**
- Cole o token do bot

**5. Ativar o workflow**
- Clique no toggle **Inactive → Active**
- O workflow roda automaticamente a cada 5 minutos

### Exemplos de mensagens enviadas

**Quando o site cai:**
```
🚨 ALERTA: Site fora do ar!
🌐 URL: https://seu-site.com
⏰ Horário: 07/05/2026 14:35:00
📊 Status: 503
⚠️ Verifique imediatamente!
```

**Quando o site volta:**
```
✅ Site voltou ao ar!
🌐 URL: https://seu-site.com
⏰ Horário: 07/05/2026 14:40:00
📊 Status: 200 OK
✨ Tudo funcionando normalmente.
```

### Por que este projeto é relevante para cybersecurity?

Monitoramento de disponibilidade é uma das tarefas mais básicas em **operações de segurança (SecOps)**. Sites fora do ar podem indicar ataques **DDoS**, comprometimento de servidor ou falhas de infraestrutura. Este workflow simula um **alerting system** similar ao que equipes de SOC utilizam com ferramentas como PagerDuty ou Nagios.

---

## Projeto 3 — Threat Intel Diário com IA e Email Digest

### O que o projeto faz

Todo dia às **8h da manhã**, o workflow:
1. Lê **3 feeds RSS** de sites referência em cybersecurity
2. Filtra apenas as notícias das **últimas 24 horas**
3. Usa a **OpenAI** para resumir cada notícia e classificar a criticidade (ALTA / MÉDIA / BAIXA)
4. Envia um **email HTML formatado** via Gmail com o digest completo

### Diagrama do fluxo

```
Schedule 8h → RSS Feed (x3) → Merge → Filtrar 24h → Tem notícias?
                                                           ↓ SIM
                                                    OpenAI (resume + classifica)
                                                           ↓
                                                    Gmail (digest HTML)
```

### Nodes utilizados

| # | Node | Função |
|---|------|--------|
| 1 | **Schedule Trigger** | Dispara todo dia às 8:00 (cron: `0 8 * * *`) |
| 2-4 | **RSS Feed (x3)** | Lê The Hacker News, Bleeping Computer e KrebsOnSecurity |
| 5-6 | **Merge (x2)** | Une todos os artigos dos 3 feeds em uma lista única |
| 7 | **Code / Filter** | Descarta artigos com mais de 24h; prepara o prompt para a IA |
| 8 | **IF (Tem notícias?)** | Se não há notícias novas, encerra sem enviar email |
| 9 | **OpenAI** | Resume cada notícia e classifica a criticidade |
| 10 | **Gmail** | Envia o digest HTML formatado para o email configurado |

### Fontes monitoradas

| Feed | URL |
|------|-----|
| The Hacker News | `https://feeds.feedburner.com/TheHackersNews` |
| Bleeping Computer | `https://www.bleepingcomputer.com/feed/` |
| KrebsOnSecurity | `https://krebsonsecurity.com/feed/` |

Essas três fontes são referências mundiais em cybersecurity e publicam diariamente sobre vulnerabilidades, ataques, patches e incidentes de segurança.

### Como a IA classifica as notícias

O **prompt enviado à OpenAI** instrui o modelo a:
- **Resumir** a notícia em 2-3 frases claras e objetivas
- **Classificar a criticidade** com base no impacto potencial:
  - `ALTA` — vulnerabilidade crítica (0-day, ransomware ativo, exploração em massa)
  - `MÉDIA` — patch importante, campanha de phishing, incidente localizado
  - `BAIXA` — notícia informativa, estudo de caso, tendência de mercado

### Passo a passo para configurar

**1. Importar o workflow**
- **Workflows > Import from File** → `workflow-threat-intel-diario.json`

**2. Configurar credencial OpenAI**
- No node **OpenAI Resume e classifica**
- Selecione ou crie uma credencial **OpenAI API** com sua chave

**3. Configurar credencial Gmail**
- No node **Enviar email digest**
- Crie uma credencial **Gmail OAuth2**
- Autorize o acesso à sua conta Google

**4. Definir o email de destino**
- No node Gmail, configure o campo `To` com o email que receberá o digest

**5. Ativar o workflow**
- Toggle **Inactive → Active**
- O workflow rodará sozinho toda manhã às 8h

### Exemplo do email gerado

```
🛡️ Threat Intel Diário — 07/05/2026 (12 notícias)

[CRITICIDADE: ALTA] Ransomware ataca hospitais nos EUA
Resumo: Grupo LockBit 3.0 comprometeu sistemas de 5 hospitais...
🔗 Leia a notícia completa

[CRITICIDADE: MÉDIA] Patch Tuesday — Microsoft corrige 78 vulnerabilidades
Resumo: A Microsoft lançou atualizações de segurança para...
🔗 Leia a notícia completa

─────────────────────────────
Briefing Executivo do Dia
O cenário de ameaças desta semana é dominado por campanhas de ransomware...
```

### Por que este projeto é relevante para cybersecurity?

**Threat Intelligence (TI)** é a prática de coletar, analisar e agir sobre informações de ameaças cibernéticas. Analistas de segurança gastam horas diariamente lendo feeds e relatórios. Este workflow automatiza a parte de **coleta e triagem**, permitindo que o analista foque apenas no que é **ALTA criticidade** — exatamente o que ferramentas enterprise como **ThreatConnect, Recorded Future e MISP** fazem, mas de forma acessível e customizável.

---

## Configuração Geral do Ambiente

### Pré-requisitos

- n8n instalado (via Docker, npm ou conta em cloud.n8n.io)
- Conta na OpenAI com chave de API ativa
- Conta Google (para Google Sheets e Gmail)
- Conta no Telegram com um bot criado via @BotFather

### Variáveis de ambiente necessárias

Copie o arquivo `.env.example` para `.env` e preencha com seus dados reais:

```env
# OpenAI
OPENAI_API_KEY=sk-proj-SuaChaveAqui

# Google Sheets (Projeto 1)
GOOGLE_SHEET_ID=ID_da_planilha_na_URL

# Telegram (Projeto 2)
TELEGRAM_BOT_TOKEN=token_gerado_pelo_BotFather
TELEGRAM_CHAT_ID=seu_chat_id

# Gmail (Projeto 3)
EMAIL_DESTINO=seuemail@gmail.com
```

> **NUNCA** commite o arquivo `.env` no Git. Ele está listado no `.gitignore` por segurança.

---

## Perguntas e Respostas sobre os Projetos

### Sobre o n8n e automação

**1. O que é um workflow no n8n e qual a diferença entre um Trigger e um Node comum?**

> Um **workflow** é uma sequência de tarefas conectadas que o n8n executa. O **Trigger** é o node especial que **inicia** o workflow — pode ser manual (clique), agendado (cron), por webhook, etc. Os demais nodes são ações que processam e transformam os dados recebidos do trigger.

**2. Por que usar o n8n em vez de simplesmente escrever um script Python?**

> O n8n oferece **interface visual**, facilitando a manutenção e o entendimento do fluxo por pessoas que não são desenvolvedoras. Além disso, possui **centenas de integrações prontas** (Google, Telegram, OpenAI, etc.) sem precisar gerenciar autenticação manualmente. Para tarefas recorrentes e integrações múltiplas, o n8n reduz muito o tempo de desenvolvimento.

**3. O que é o Schedule Trigger e como ele funciona internamente?**

> O Schedule Trigger usa expressões **cron** para definir quando o workflow será disparado. Por exemplo, `0 8 * * *` significa "todo dia às 8h". O n8n mantém um processo rodando em background que verifica o horário e dispara o workflow no momento correto, sem intervenção humana.

**4. Como o n8n guarda o "estado" entre execuções (como no Projeto 2)?**

> O n8n tem um recurso de **Static Data** (dados estáticos por workflow) que persiste entre execuções. No Projeto 2, o estado anterior do site (online/offline) é salvo nesse armazenamento interno, permitindo que a próxima execução compare com o estado atual e decida se deve ou não enviar a notificação.

---

### Sobre o Projeto 1 — OpenAI + Google Sheets

**5. Por que o campo "fonte" é necessário na planilha?**

> O campo `fonte` identifica **de onde veio a informação** — neste caso, da OpenAI GPT. Em sistemas reais de Threat Intelligence, registrar a fonte é obrigatório para avaliar a **confiabilidade** da informação e rastrear sua origem.

**6. O que aconteceria se a API da OpenAI ficasse fora do ar?**

> O node do HTTP Request (OpenAI) retornaria um erro e a execução do workflow falharia. Para produção, seria ideal adicionar um node de **tratamento de erros** (Error Trigger) que notificasse o responsável sobre a falha.

---

### Sobre o Projeto 2 — Monitoramento de Site

**7. Por que o HTTP Request está configurado para "não quebrar" quando o site não responde?**

> A opção **"Continue on Fail"** faz com que o node passe adiante mesmo com erro (timeout, conexão recusada). Sem essa configuração, se o site estivesse fora do ar, o próprio workflow quebraria antes de conseguir enviar o alerta — o que é contraproducente, já que o objetivo é **detectar a queda**.

**8. O que é um código HTTP 200, 4xx e 5xx?**

> São códigos de status HTTP que indicam o resultado de uma requisição:
> - **200 OK** — site respondendo normalmente
> - **4xx** — erro do cliente (ex: 404 = página não encontrada, 403 = acesso negado)
> - **5xx** — erro do servidor (ex: 500 = erro interno, 503 = serviço indisponível)
> O Projeto 2 considera qualquer código diferente de 200 como uma possível queda.

**9. Por que o sistema só envia UMA notificação de queda e não uma a cada 5 minutos?**

> Porque o workflow **compara o estado atual com o estado anterior**. Na primeira execução após a queda, o estado muda de "online" para "offline" → envia alerta. Nas execuções seguintes, o site continua offline, mas o estado **não mudou** → nenhuma notificação. Isso evita spam e garante que o alerta seja acionável.

---

### Sobre o Projeto 3 — Threat Intel

**10. O que é um RSS Feed e por que é usado em Threat Intelligence?**

> **RSS (Really Simple Syndication)** é um formato padronizado de distribuição de conteúdo. Sites de notícias publicam seus artigos em XML, e qualquer aplicação pode consumir esse feed sem precisar de uma API específica. Em Threat Intelligence, RSS é amplamente usado para **monitorar fontes confiáveis** (blogs de pesquisa, CVEs, boletins de segurança) de forma automatizada.

**11. Como a OpenAI consegue classificar a criticidade das notícias? Isso é confiável?**

> O modelo de linguagem (GPT) é instruído via **prompt de sistema** a avaliar palavras-chave e contexto: "zero-day explorado ativamente" → ALTA; "patch recomendado" → MÉDIA; "artigo educacional" → BAIXA. Não é 100% confiável para uso em produção sem revisão humana, mas serve como **triagem inicial** eficiente, reduzindo o volume de leitura manual em até 80%.

**12. O que acontece se não houver notícias nas últimas 24h?**

> O node **"Tem notícias?"** (IF) verifica se a lista filtrada está vazia. Se sim, o workflow termina sem executar a IA e sem enviar email — economizando tokens da OpenAI e evitando emails vazios na caixa de entrada.

**13. Por que escolher The Hacker News, Bleeping Computer e KrebsOnSecurity?**

> São três das fontes mais respeitadas e atualizadas em cybersecurity:
> - **The Hacker News** — cobertura ampla e rápida de ameaças globais
> - **Bleeping Computer** — foco em malware, ransomware e ataques práticos
> - **KrebsOnSecurity** — investigação jornalística profunda, especialista em crimes cibernéticos

---

### Sobre boas práticas e segurança

**14. Por que as credenciais não ficam no código (no JSON do workflow)?**

> Deixar chaves de API diretamente no código é uma **vulnerabilidade grave** (CWE-798 - Use of Hard-coded Credentials). Se o repositório for público ou vazar, qualquer pessoa pode usar suas credenciais. O n8n salva as credenciais criptografadas no seu vault interno, e o `.env` com chaves reais nunca é commitado no Git (protegido pelo `.gitignore`).

**15. O que é o `.gitignore` e qual a importância dele neste projeto?**

> O `.gitignore` é um arquivo que diz ao Git **quais arquivos devem ser ignorados** e nunca enviados para o repositório. Neste projeto, ele garante que o arquivo `.env` (com chaves de API reais) e arquivos de credenciais nunca sejam acidentalmente publicados no GitHub — uma boa prática fundamental de segurança no desenvolvimento.

---

## Aprendizados da Semana

Ao longo desta semana, foram praticados e consolidados os seguintes conceitos:

| Competência | Aplicação prática |
|-------------|-------------------|
| **Automação com n8n** | Criação de 3 workflows funcionais do zero |
| **Integração com APIs** | OpenAI, Telegram, Google Sheets e Gmail OAuth2 |
| **Lógica condicional em workflows** | Switch, IF, tratamento de estados |
| **Agendamento de tarefas** | Cron expressions para execuções periódicas |
| **Threat Intelligence básica** | Coleta, filtragem e triagem automatizada de feeds |
| **Boas práticas de segurança** | Uso de `.gitignore`, `.env`, vaults de credenciais |
| **Documentação técnica** | README detalhado para cada projeto |

---

*Repositório desenvolvido como parte da Trilha Kensei Cybersecurity — Semana 5 | 2026*
