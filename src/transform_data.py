import pandas as pd
from pathlib import Path
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

path_name = Path(__file__).resolve().parent.parent / 'data' / 'weather_data.json'

columns_names_to_drop = ['weather','weather_icon','sys.type']
columns_names_to_rename = {
        "base": "base",
        "visibility": "visibility",
        "dt": "datetime",
        "timezone": "timezone",
        "id": "city_id",
        "name": "city_name",
        "cod": "code",
        "coord.lon": "longitude",
        "coord.lat": "latitude",
        "main.temp": "temperature",
        "main.feels_like": "feels_like",
        "main.temp_min": "temp_min",
        "main.temp_max": "temp_max",
        "main.pressure": "pressure",
        "main.humidity": "humidity",
        "main.sea_level": "sea_level",
        "main.grnd_level": "grnd_level",
        "wind.speed": "wind_speed",
        "wind.deg": "wind_deg",
        "wind.gust": "wind_gust",
        "clouds.all": "clouds",
        "sys.type": "sys_type",
        "sys.id": "sys_id",
        "sys.country": "country",
        "sys.sunrise": "sunrise",
        "sys.sunset": "sunset",
        # weather_id, weather_main, weather_description
    }
columns_normalize_datetime = {'datetime','sunrise','sunset'}

def create_df(path_name:str) -> pd.DataFrame:  ### Usando o pacote pathlib passo o caminho de onde está o meu json
    logging.info('Criando dataframe...')
    path = path_name  ### coloco esse caminho em uma variavel

    if not path.exists():
        raise FileNotFoundError(f'File {path} does not exist') ### usando o logging, caso haja algum erro com o arquivo não existe, ele passa um alerta

    with open(path_name) as f:  ### usando o json, passo o caminho para que o arquivo seja passado para uma variável
        data = json.load(f)


    df = pd.json_normalize(data) ### usando o pandas, crio uma variável que pegará a variável que carregou o json e passo para normalizar ele para um dataframe
    logging.info(f'\n Dataframe criado com {len(df)} linhas')
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apesar de ter normalizado algumas colunas ainda ficam erradas, então crio
    uma função que vai receber o meu dataframe como um dataframe.
    """
    df_weather = pd.json_normalize(df['weather'].apply(lambda x: x[0]))


    '''
    crio um novo dataframe usando meu original mas filtrando para que seja apenas a colunas weather, uso o normalize 
    para que ele faça apenas na primeira coluna 'weather' porém passando uma função lambda para que pegue apenas o primeiro 
    item.
    '''


    df_weather = df_weather.rename(columns={
        'id':'weather_id',
        'main':'weather_main',
        'description':'weather_description',
        'icon':'weather_icon',

    })

    df = pd.concat([df, df_weather], axis=1)
    logging.info(f'\n Dataframe normalizado com {len(df.columns)} colunas')
    return df


def drop_columns(df: pd.DataFrame, columns_names:list[str]) -> pd.DataFrame:
    logging.info('Dropando colunas...')
    df = df.drop(columns=columns_names)
    logging.info('Colunas dropadas com sucesso')

    return df


def rename_columns(df: pd.DataFrame, columns_names:dict[str,str]) -> pd.DataFrame:
    df = df.rename(columns=columns_names)
    return df


def normalize_datatime_columns(df: pd.DataFrame, columns_name:list[str]) -> pd.DataFrame:
    for name in columns_name:
        df[name] = pd.to_datetime(df[name], unit='s', utc=True).dt.tz_convert('America/Sao_Paulo')

    return df


def data_transformation():

    print('\n Transformando dados...')

    df = create_df(path_name)
    df = normalize_columns(df)
    df = drop_columns(df, columns_names_to_drop)
    df = rename_columns(df, columns_names_to_rename)
    df = normalize_datatime_columns(df, columns_normalize_datetime)

    logging.info('Tranformçãoes Concluidas')

    return df
