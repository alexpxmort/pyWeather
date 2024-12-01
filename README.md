### README.md

# Weather ETL API

## Descrição

Este projeto é uma API para processar e consultar dados meteorológicos utilizando um pipeline ETL. Os dados extraídos são processados, armazenados em um banco de dados e disponibilizados para consulta através de diversos endpoints.

## Endpoints Disponíveis

### 1. **`GET /etl`**
Executa o pipeline ETL para as cidades Rio de Janeiro, Curitiba e São Paulo.  
- **Processo:** 
  1. Extração dos dados meteorológicos via API.
  2. Processamento dos dados extraídos.
  3. Armazenamento dos dados no banco.
- **Resposta:** Retorna o status do processo para cada cidade.
- **Exemplo de Resposta:**
  ```json
  [
    {"city": "Rio de Janeiro", "status": "success", "message": "Dados para Rio de Janeiro inseridos com sucesso!"},
    {"city": "Curitiba", "status": "success", "message": "Dados para Curitiba inseridos com sucesso!"},
    {"city": "São Paulo", "status": "success", "message": "Dados para São Paulo inseridos com sucesso!"}
  ]
  ```

---

### 2. **`GET /cities`**
Lista todas as cidades cadastradas no banco de dados.  
- **Resposta:** Uma lista de cidades com seus IDs e nomes.
- **Exemplo de Resposta:**
  ```json
  [
    {"id": 1, "name": "Rio de Janeiro"},
    {"id": 2, "name": "Curitiba"},
    {"id": 3, "name": "São Paulo"}
  ]
  ```

---

### 3. **`GET /weather/hot-cities`**
Lista cidades onde a temperatura foi superior a 25°C.  
- **Resposta:** Lista de cidades e suas temperaturas.
- **Exemplo de Resposta:**
  ```json
  [
    {"city": "Rio de Janeiro", "temperature": 30.5},
    {"city": "São Paulo", "temperature": 26.2}
  ]
  ```

---

### 4. **`GET /weather/avg-temperature`**
Calcula a temperatura média por cidade.  
- **Resposta:** Lista de cidades com suas temperaturas médias.
- **Exemplo de Resposta:**
  ```json
  [
    {"city": "Rio de Janeiro", "avg_temperature": 27.4},
    {"city": "Curitiba", "avg_temperature": 22.1}
  ]
  ```

---

### 5. **`GET /daily_summary`**
Lista os resumos diários dos dados meteorológicos por cidade.  
- **Resposta:** Resumos com informações como temperatura média, umidade média, e total de registros.
- **Exemplo de Resposta:**
  ```json
  [
    {
      "city_name": "Rio de Janeiro",
      "date": "2024-12-01",
      "avg_temperature": 27.5,
      "avg_humidity": 60,
      "record_count": 50
    }
  ]
  ```

---

### 6. **`GET /weather`**
Lista todas as informações climáticas registradas no banco.  
- **Resposta:** Detalhes climáticos como temperatura, umidade, condição climática, entre outros.
- **Exemplo de Resposta:**
  ```json
  [
    {
      "city": "São Paulo",
      "country": "Brazil",
      "latitude": -23.5505,
      "longitude": -46.6333,
      "temperature": 25.3,
      "humidity": 70,
      "timestamp": "2024-12-01 09:00:00",
      "windspeed": 12.5,
      "weather_condition": "Clear",
      "precipitation": 0
    }
  ]
  ```

---

### 7. **`GET /generate_summary`**
Gera o resumo diário para todas as cidades.  
- **Processo:** Consolida os dados meteorológicos do dia, calculando médias e agregados.
- **Resposta:** Retorna uma mensagem de sucesso.
- **Exemplo de Resposta:**
  ```json
  {"message": "Resumo diário gerado com sucesso!"}
  ```

---


## Configuração e Execução do Airflow

Para iniciar o Airflow, siga as etapas abaixo:

1. **Inicializar o banco de dados do Airflow**:

   Antes de iniciar os serviços, inicialize o banco de dados do Airflow (caso seja a primeira vez que você está rodando o Airflow):

   ```bash
   airflow db init
   ```

2. **Iniciar o Webserver do Airflow**:

   Para iniciar o servidor web do Airflow e acessar a interface web, execute:

   ```bash
   airflow webserver --port 8080
   ```

   O servidor web do Airflow será iniciado e você poderá acessar a interface web na URL `http://localhost:8080`.

3. **Iniciar o Scheduler do Airflow**:

   O Airflow precisa de um scheduler para monitorar e executar os DAGs. Para iniciar o scheduler, execute:

   ```bash
   airflow scheduler
   ```

   O scheduler irá verificar os DAGs configurados e executá-los conforme o cronograma (schedule).

## Cronograma (Schedule)

O pipeline ETL neste projeto é configurado para ser executado a cada 5 minutos, como definido no arquivo de configuração do DAG. Você pode ajustar o cronograma conforme necessário. No arquivo do DAG, o `schedule_interval` é configurado da seguinte maneira:

```python
schedule_interval='*/5 * * * *',  # Executa a cada 5 minutos
```

Se quiser que o pipeline seja executado em outro intervalo, pode alterar a string `schedule_interval` para o valor desejado. Por exemplo:

- `@daily`: Executa uma vez por dia.
- `0 9 * * *`: Executa diariamente às 9h.
- `*/10 * * * *`: Executa a cada 10 minutos.

## Acessando a Interface Web do Airflow

Após iniciar o servidor web com o comando acima, você pode acessar a interface do Airflow no seu navegador em `http://localhost:8080`. O Airflow tem uma interface web bastante amigável onde você pode monitorar, ativar, desativar e visualizar o status de seus DAGs.

## Configuração do Projeto

1. **Banco de Dados:** Certifique-se de configurar corretamente as informações do banco no arquivo `config.py`.
2. **ETL Scripts:** Os scripts para extração, processamento e carga estão localizados no diretório `scripts`.

## Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute as migrações do banco:
   ```bash
   flask db upgrade
   ```
3. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
4. Acesse os endpoints em `http://localhost:5000`.

---

## Tecnologias Utilizadas

- **Flask:** Framework para desenvolvimento web.
- **SQLAlchemy:** ORM para interação com o banco de dados.
- **Flask-Migrate:** Gerenciamento de migrações do banco.
- **MySQL:** Banco de dados relacional para armazenamento dos dados.

## Autor

Projeto desenvolvido para fins educativos.
