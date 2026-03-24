from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

# Conecta no banco
load_dotenv()
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)

# Query da View 1: Média de temperatura
view1 = """
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;
"""

# Query da View 2: Leituras por hora do dia
view2 = """
CREATE OR REPLACE VIEW leituras_por_hora AS
SELECT CAST(SUBSTRING(data_hora, 12, 2) AS INTEGER) as hora, COUNT(*) as contagem
FROM temperature_readings
GROUP BY CAST(SUBSTRING(data_hora, 12, 2) AS INTEGER);
"""

# Query da View 3: Máxima e mínima por dia
view3 = """
CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT SUBSTRING(data_hora, 1, 10) as data, MAX(temperature) as temp_max, MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY SUBSTRING(data_hora, 1, 10);
"""

print("⏳ Criando as Views no PostgreSQL...")

# Executa os comandos no banco de dados
with engine.connect() as conn:
    conn.execute(text(view1))
    conn.execute(text(view2))
    conn.execute(text(view3))
    conn.commit() # Salva as alterações

print("✅ SUCESSO! As 3 Views foram criadas e estão prontas para o Dashboard!")