temperaturas = [25, 31, 29, 33]
alarmas = 0
for temperatura in temperaturas:
    if temperatura > 30:
        alarmas += 1
print(alarmas)
