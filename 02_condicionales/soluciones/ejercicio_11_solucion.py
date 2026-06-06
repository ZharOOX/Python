conectado = False
temperatura = 35
if not conectado:
    print("ERROR SENSOR")
elif temperatura > 30:
    print("ALTA")
else:
    print("OK")
