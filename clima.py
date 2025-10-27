from datetime import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

def clima_agora(local):
    """
    Consulta a API OpenWeather (One Call) para obter dados do clima atual
    a partir da string local "lat,lon" 

    Args:
        local (str): string com "lat,lon" ou None.

    Returns:
        dict | None: dicionário com os campos filtrados:
            {
                "temperatura": str,
                "sensacao_termica": str,
                "vento": str,
                "descricao": str
            }
        ou None em caso de erro.
    """

    if not API_KEY:
        print("Erro, Chave não encontrada no .env")
        return None

    lat_str, lon_str = local['local'].strip().split(',')
    try:
        lat = float(lat_str)
        lon = float(lon_str)
    except ValueError:
        print("Erro ao converter Latitude/ longitude", lat_str, lon_str)
        return None
    
    exclude = 'minutely,hourly,daily,alerts'
    units= 'metric'
    url= f'https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&units={units}&appid={API_KEY}'
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


    print (f'Conultando clima em {local['cidade']} lat= {lat}, lon={lon}')
    try:
        resposta = requests.get(url, timeout=8)
        resposta.raise_for_status()
        dados = resposta.json()

        dados_clima = dados.get('current')

        if not dados_clima:
            print("Resposta da API não contém 'Current'")
            return None
        
        weather_list = dados_clima.get('weather')
        if isinstance(weather_list,list) and len(weather_list)>0:
            descricao = weather_list[0].get('description')

        clima_atual = {
            'temperatura': f"{dados_clima.get('temp')}°C",
            'sensacao_termica': f"{dados_clima.get('feels_like')}°C",
            'vento':f"{dados_clima.get('wind_speed')} m/s",
            'descricao': descricao
        }
        
        return clima_atual, agora
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao consultar OpenWeather: {http_err} (status: {getattr(http_err.response, 'status_code', 'N/A')})")
    except requests.exceptions.Timeout:
        print("Tempo de conexão excedido ao consultar OpenWeather.")
    except requests.exceptions.RequestException as req_err:
        print("Erro de requisição:", req_err)
    except ValueError as json_err:
        print("Erro ao interpretar JSON:", json_err)
        return None