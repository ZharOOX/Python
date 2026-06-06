"""
Ejercicio 03 - Celsius a Fahrenheit

Objetivo:
Practicar operaciones aritmeticas y guardar el resultado de una conversion.

Conceptos:
- variables y tipos basicos
- print/input y conversiones cuando corresponda
- lecturas simuladas de sensores y reportes

Instrucciones:
Crea una variable `celsius` con una temperatura fija. Calcula `fahrenheit` usando la formula `fahrenheit = celsius * 9 / 5 + 32`. Imprime ambas temperaturas.

Ejemplo de entrada:
No uses input. Usa un valor fijo para `celsius`.

Ejemplo de salida:
25 C = 77.0 F

Restricciones:
- Debes definir `celsius` y `fahrenheit`. Usa exactamente la formula indicada.
- No mirar la solucion antes de intentar.
- Mantener nombres de variables si el test los necesita.

Pistas:
1. Primero guarda el valor en Celsius.
2. Luego crea otra variable para el resultado en Fahrenheit.
3. Si el calculo no coincide, revisa el orden de multiplicacion, division y suma.

Reto extra:
Prueba con 0 C y 100 C.
"""

# =========================
# ZONA DE TRABAJO
# =========================
# Escribe tu codigo aqui

celsius = 20
fahrenheit = celsius * 9 / 5 + 32
print(f"la temperatura en celcius es: {celsius}")
print(f"La temperatura en fahrenheit es: {fahrenheit}")