nombre_sensor = "TEMP_SIM_INPUT"
temperatura = float(input("Temperatura C: "))
umbral = 30.0
alerta_activa = temperatura > umbral

print("SIMULADOR DE TEMPERATURA CON INPUT")
print(f"Sensor: {nombre_sensor}")
print(f"Temperatura: {temperatura} C")
print(f"Umbral: {umbral} C")
print(f"Alerta activa: {alerta_activa}")
