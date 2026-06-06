voltaje = 3.2
conectado = True
temperatura = 29
if not conectado:
    estado = "SIN SENSOR"
elif voltaje < 3.3:
    estado = "BATERIA CRITICA"
elif temperatura > 30:
    estado = "TEMP ALTA"
else:
    estado = "OK"
print(estado)
