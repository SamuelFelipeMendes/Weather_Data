import pandas as pd
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

path_name = Path(__file__).resolve().parent / 'data' / 'weather_data.json'

def create_df(path_name:str) -> pd.DataFrame:  ### Usando o pacote pathlib passo o caminho de onde está o meu json
    path = Path(path_name)  ### coloco esse caminho em uma variavel

    if not path.exists():
        raise FileNotFoundError(f'File {path_name} does not exist') ### usando o logging, caso haja algum erro com o arquivo não existe, ele passa um alerta

    with open(path_name) as f:  ### usando o json, passo o caminho para que o arquivo seja passado para uma variável
        data = json.load(f)


    df = pd.json_normalize(data) ### usando o pandas, crio uma variável que pegará a variável que carregou o json e passo para normalizar ele para um data frame
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apesar de ter normalizado algumas colunas ainda ficam erradas, então crio
    uma função que vai receber o meu dataframe como um dataframe.
    """
    df_weather = pd.json_normalize(df['weather'].apply(lambda x: x[0]))

    """
    crio um novo dataframe usando meu original mas filtrando para que seja apenas a colunas weather, uso o normalize 
    para que ele faça apenas na primeira coluna 'weather' porém passando uma função lambda para que pegue apenas o primeiro 
    item.
    """

    df_weather = df_weather.rename(columns={
        'id':'weather_id',
        'main':'weather_main',
        'description':'weather_description',
        'icon':'weather_icon',

    })

    df = pd.concat([df, df_weather], axis=1)
    return df