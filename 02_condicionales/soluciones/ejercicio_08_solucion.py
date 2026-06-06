modo = "auto"
temperatura = 32
umbral = 30
if modo == "auto" and temperatura > umbral:
    print("VENTILADOR_ON")
else:
    print("VENTILADOR_OFF")
