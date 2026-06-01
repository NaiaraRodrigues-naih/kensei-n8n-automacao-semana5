# Automacao com n8n - Semana 5

Kensei CyberSec Lab | AI Foundations 2026

5 workflows de automacao construidos com n8n durante a Semana 5 — do primeiro workflow ate um monitor de seguranca com IA.

---

## O que e n8n?

n8n e uma plataforma de automacao low-code que conecta apps, APIs e servicos sem escrever codigo do zero. Cada no e uma acao — voce conecta os nos e cria fluxos que rodam sozinhos.

---

## Projetos

### Projeto 1 - Seu Primeiro Workflow
Primeiro contato com n8n: workflow simples com trigger manual, transformacao de dados e saida formatada.
Conceitos: nos basicos, execucao manual, debug de dados.

### Projeto 2 - Notificador de Site Down
Monitor que verifica periodicamente se um site esta online e dispara notificacao ao detectar falha.
Conceitos: HTTP Request, condicional IF, Cron, alertas automaticos.

### Projeto 3 - Threat Intel Diario com IA
Pipeline automatizado que coleta inteligencia de ameacas e usa IA para gerar resumo diario de seguranca.
Conceitos: feeds de threat intel, processamento com IA, relatorio automatico.

### Projeto 4 - API Pessoal com Webhook
Endpoint proprio criado no n8n via Webhook: recebe dados, processa e responde sem servidor dedicado.
Conceitos: Webhook trigger, payload JSON, resposta HTTP customizada.

### Projeto Pessoal - Monitor de E-mail Vazado
Automacao que verifica se e-mails estao em bases de dados de vazamentos e notifica o resultado.
Conceitos: API de breach, logica condicional, notificacao personalizada.

---

## Como usar

Pre-requisitos: n8n instalado localmente ou conta em n8n.io

Instalacao local:
  npm install -g n8n
  n8n start

Importar workflow:
1. Abra n8n em http://localhost:5678
2. Va em Workflows > Import
3. Selecione o .json do projeto
4. Configure as credenciais
5. Ative e teste

Credenciais: copie .env.example para .env e preencha com suas chaves.

---

Feito com dedicacao por Naiara Rodrigues
Kensei CyberSec Lab | AI Foundations 2026