alertas = 0
suma = 0
for i in range(10):
    temperatura = 24 + i
    suma += temperatura
    if temperatura > 30:
        alertas += 1
print(f"Promedio: {suma / 10}")
print(f"Alertas: {alertas}")
