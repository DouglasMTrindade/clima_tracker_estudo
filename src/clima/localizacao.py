import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('IPINFO_API_KEY')

def busca_localizacao ():
    """
    Busca a localização atual baseada no IP usando a API do ipinfo.io.
    
    Returns:
        dict: Dados da localização (cidade, região, país, lat/long, etc.) ou None em caso de erro
    """

    if not API_KEY:
        print("Erro, chave nao entrada no .env")
        return None
    
    url = f'https://ipinfo.io/json?token={API_KEY}'

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        dados_local = {
            'cidade': dados['city'],
            'local': dados['loc']
        }
        return dados_local
    except requests.exceptions.RequestException as e:
        print("Erro: ",e)
        return None

