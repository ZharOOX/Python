temperaturas = [25, 31, 29]
humedades = [50, 80, 40]
alertas = 0
for temperatura, humedad in zip(temperaturas, humedades):
    if temperatura > 30 or humedad > 75:
        alertas += 1
print(alertas)
