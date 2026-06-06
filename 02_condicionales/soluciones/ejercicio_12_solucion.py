modo = "manual"
comando = "LED_ON"
temperatura = 25
if modo == "manual":
    salida = comando == "LED_ON"
else:
    salida = temperatura > 30
print(salida)
