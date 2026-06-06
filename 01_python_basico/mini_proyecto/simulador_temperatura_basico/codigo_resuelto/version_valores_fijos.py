nombre_sensor = "TEMP_SIM_01"
temperatura = 31.2
umbral = 30.0
alerta_activa = temperatura > umbral

print("SIMULADOR DE TEMPERATURA")
print(f"Sensor: {nombre_sensor}")
print(f"Temperatura: {temperatura} C")
print(f"Umbral: {umbral} C")
print(f"Alerta activa: {alerta_activa}")
