import requests
import json
import os
from pathlib import Path

# Carrega o .env da raiz do projeto (um nível acima desta pasta)
env_path = Path(__file__).parent.parent / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                os.environ.setdefault(key.strip(), value.strip())

# Lê do .env; se não existir, usa localhost como padrão
WEBHOOK_URL = os.environ.get(
    "WEBHOOK_URL",
    "http://localhost:5678/webhook/sentiment"
)

casos_de_teste = [
    {
        "descricao": "Texto positivo",
        "payload": {"texto": "Adorei o curso da Kensei! O conteudo e incrivel e aprendi muito."}
    },
    {
        "descricao": "Texto negativo",
        "payload": {"texto": "Pessimo servico, nunca mais compro nessa loja. Fui enganado."}
    },
    {
        "descricao": "Texto neutro",
        "payload": {"texto": "O produto chegou na data prevista e veio na embalagem correta."}
    },
    {
        "descricao": "Texto misto/complexo",
        "payload": {"texto": "O preco e bom mas a entrega demorou demais e o atendimento foi ok."}
    }
]


def testar(descricao, payload):
    print(f"\n{'='*55}")
    print(f"Teste: {descricao}")
    print(f"Texto: \"{payload['texto'][:60]}...\"" if len(payload['texto']) > 60 else f"Texto: \"{payload['texto']}\"")

    try:
        response = requests.post(
            WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        if response.status_code == 200:
            resultado = response.json()
            print(f"Status: {response.status_code} OK")
            print(f"Sentimento:     {resultado.get('sentimento', 'N/A')}")
            print(f"Confianca:      {resultado.get('confianca', 'N/A')}")
            print(f"Palavras-chave: {resultado.get('palavras_chave', [])}")
            print(f"JSON completo:  {json.dumps(resultado, ensure_ascii=False)}")
        else:
            print(f"Erro HTTP {response.status_code}: {response.text}")

    except requests.exceptions.ConnectionError:
        print("ERRO: Nao foi possivel conectar ao n8n.")
        print("Verifique se o n8n esta rodando e se o webhook esta ativo.")
    except requests.exceptions.Timeout:
        print("ERRO: Timeout - o n8n demorou mais de 30 segundos para responder.")
    except Exception as e:
        print(f"ERRO inesperado: {e}")


def testar_texto_customizado():
    print(f"\n{'='*55}")
    print("TESTE CUSTOMIZADO")
    texto = input("Digite um texto para analisar: ").strip()
    if texto:
        testar("Texto customizado", {"texto": texto})
    else:
        print("Texto vazio, pulando...")


if __name__ == "__main__":
    print("TESTADOR DA API DE SENTIMENTOS - Projeto 4")
    print(f"URL: {WEBHOOK_URL}")
    print("\nCertifique-se que o workflow esta ativo no n8n antes de testar.")

    for caso in casos_de_teste:
        testar(caso["descricao"], caso["payload"])

    testar_texto_customizado()

    print(f"\n{'='*55}")
    print("Testes finalizados.")
