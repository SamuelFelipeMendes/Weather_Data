#  Weather_Data

Projeto de exemplo de pipeline de dados para obtenção de informações meteorológicas usando a API do **OpenWeatherMap**.

Este projeto demonstra um fluxo simples de **Extração → Transformação → Carga (ETL)** de dados climáticos para posterior uso em bases de dados ou análises.

---

##  Estrutura do final do Projeto

##  Tecnologias

### Core

<ol> 
  <li> Python 3.14+ - Linguagem principal </li>
  <li> Apache Airflow 3.1.7 - Orquestração do pipeline </li>
  <li> PostgreSQL 14 - Banco de dados relacional </li>
  <li> Docker & Docker Compose - Containerização </li>
</ol>

### Bibliotecas Python
<ol> 
  <li> pandas - Manipulação e transformação de dados </li>
  <li> requests - Requisições HTTP para a API </li>
  <li> SQLAlchemy - ORM para interação com o banco de dados </li>
  <li> psycopg2 - Driver PostgreSQL </li>
  <li> python-dotenv - Gerenciamento de variáveis de ambiente </li>
</ol>

##  Descrição

O projeto realiza o seguinte fluxo:

1. **Extrai** dados de clima para uma cidade usando a API do *OpenWeatherMap*.
2. **Transforma** os dados em um formato tabular.
3. **Carrega** os dados em uma tabela destinada em um banco de dados ( banco utilizado foi o postgreslq )

## API 

A API vem de o openWeatherMap. 

É necessário que tenha uma conta para ter acesso a sua própria API.

##








