temperatura = 31
humedad = 25
voltaje = 3.8
if voltaje < 3.3:
    print("REVISAR ENERGIA")
elif temperatura > 30 and humedad < 30:
    print("CALOR SECO")
else:
    print("SISTEMA NORMAL")
