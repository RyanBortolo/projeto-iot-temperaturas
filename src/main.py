import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv


load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

print("⏳ Lendo o arquivo CSV...")

df = pd.read_csv('data/IOT-temp.csv')


df = df.rename(columns={
    'room_id/id': 'device_id',
    'temp': 'temperature',
    'noted_date': 'data_hora'
})

print("Estrutura dos dados pronta para o banco:")
print(df.head())

print("\n⏳ Enviando dados para o banco PostgreSQL (pode demorar uns segundos)...")

df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("✅ SUCESSO! Todos os dados do IoT foram inseridos no banco!")