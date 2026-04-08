
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;

SELECT CAST(SUBSTRING(data_hora, 12, 2) AS INTEGER) as hora, COUNT(*) as contagem
FROM temperature_readings
GROUP BY CAST(SUBSTRING(data_hora, 12, 2) AS INTEGER);


CREATE OR REPLACE VIEW temp_max_min_por_dia AS
SELECT SUBSTRING(data_hora, 1, 10) as data, MAX(temperature) as temp_max, MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY SUBSTRING(data_hora, 1, 10);