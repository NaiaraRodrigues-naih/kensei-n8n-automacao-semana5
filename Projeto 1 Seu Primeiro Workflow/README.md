# Projeto 1 - Workflow n8n

Workflow criado: `workflow-frase-motivacional-openai-google-sheets.json`

## O que ele faz

Ao clicar em **Manual Trigger**, o n8n:

1. chama a OpenAI para gerar uma frase motivacional curta em portugues;
2. organiza os campos `data`, `frase` e `fonte`;
3. adiciona uma nova linha em uma planilha do Google Sheets.

## Como importar no n8n

1. Abra o n8n.
2. Va em **Workflows** > **Import from File**.
3. Selecione o arquivo `workflow-frase-motivacional-openai-google-sheets.json`.
4. No node **Gerar frase com OpenAI**, selecione/crie sua credencial da OpenAI.
5. No node **Salvar no Google Sheets**, selecione/crie sua credencial do Google Sheets.
6. Confirme que a aba da planilha se chama `Frases`.

## Estrutura esperada da planilha

Crie uma aba chamada `Frases` com as colunas:

```text
data | frase | fonte
```

Depois disso, execute o workflow pelo **Manual Trigger**.
