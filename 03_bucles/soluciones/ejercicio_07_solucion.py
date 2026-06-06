alarmas = 0
for i in range(6):
    temperatura = 27 + i
    if temperatura > 30:
        alarmas += 1
print(alarmas)
