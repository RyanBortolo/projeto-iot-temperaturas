import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 1. Carrega as configurações do .env
load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

print("⏳ Lendo o arquivo CSV...")
# 2. Lê o CSV usando o nome exato que está no seu VS Code
df = pd.read_csv('data/IOT-temp.csv')

# 3. Renomeia as colunas para bater com o SQL exigido pelo professor
df = df.rename(columns={
    'room_id/id': 'device_id',
    'temp': 'temperature',
    'noted_date': 'data_hora'
})

print("Estrutura dos dados pronta para o banco:")
print(df.head())

print("\n⏳ Enviando dados para o banco PostgreSQL (pode demorar uns segundos)...")
# 4. Cria a tabela 'temperature_readings' e insere os dados
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("✅ SUCESSO! Todos os dados do IoT foram inseridos no banco!")