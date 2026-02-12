import requests
import json
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def extract_data(url:str) -> list:
    response = requests.get(url) # armazeno uma requisição get da api em uma variável
    data = response.json()       # Armazeno a variável com os dados solicitados a api em um json e armazenom em outra variável

    if response.status_code != 200:
        logging.error('Error to get from url')
        return []

    if not data:
        logging.warning('No data found')
        return []
    output_path = 'data/weather_data.json' ##Cria um arquivo weather json quando a função é chamada
    output_dir = Path(output_path).parent  ##Indica que a variável que cria o json deve retornar um arquivo
    output_dir.mkdir(parents=True, exist_ok=True) ## parents = indica que ele deve criar o caminho de diretório

    with open(output_path,'w') as f:
        json.dump(data,f,indent=4)

    logging.info(f'Arquivo json criado com sucesso em {output_path}')

    return data
