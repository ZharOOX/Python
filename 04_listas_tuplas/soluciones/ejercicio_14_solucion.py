temperaturas = [25, 31, 29, 33]
promedio = sum(temperaturas) / len(temperaturas)
alertas = 0
for temperatura in temperaturas:
    if temperatura > 30:
        alertas += 1
print(promedio, min(temperaturas), max(temperaturas), alertas)
