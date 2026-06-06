maxima = None
for i in range(5):
    lectura = 22 + i * 1.5
    if maxima is None or lectura > maxima:
        maxima = lectura
print(maxima)
