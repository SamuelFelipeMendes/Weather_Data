#  Weather_Data

Projeto de exemplo de pipeline de dados para obtenção de informações meteorológicas usando a API do **OpenWeatherMap**.

Este projeto demonstra um fluxo simples de **Extração → Transformação → Carga (ETL)** de dados climáticos para posterior uso em bases de dados ou análises.

---

##  Estrutura do final do Projeto
│   
├── config/  
│   └── .env -> config do banco e da API
├── data/
│	 └── weather_data.json -> .json extraído da API
├── notebooks/
│	 └── analysis_data.ipynb -> Visualização dos dados
├── src/
│   ├── Extract_data.py
│   ├── Load_data.py
│   └── Tranform_data.py
├── .env
├── requirements.txt
├── Teste_exe.py -> Arquivo de teste de execução
├── docker-compose.yaml
└── README.md

##  Descrição

O projeto realiza o seguinte fluxo:

1. **Extrai** dados de clima para uma cidade usando a API do *OpenWeatherMap*.
2. **Transforma** os dados em um formato tabular.
3. **Carrega** os dados em uma tabela destinada em um banco de dados ( banco utilizado foi o postgreslq )

## API 

A API vem de o openWeatherMap. 

É necessário que tenha uma conta para ter acesso a sua própria API.

##
