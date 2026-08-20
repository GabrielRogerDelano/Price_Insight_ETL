import requests

def extract(endpoint):
    response = requests.get(endpoint)

    if not response:
        print(f"Erro ao extrair dados do endpoint: {endpoint}")
        return None

    try:
        data = response.json()
    except:
        print(f"Resposta vazia ou invalida em {endpoint}")
        return None
    
    return data

