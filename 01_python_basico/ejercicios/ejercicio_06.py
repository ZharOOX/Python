"""
Ejercicio 06 - Lectura valida

Objetivo:
Practicar comparaciones booleanas con una lectura de sensor.

Conceptos:
- variables y tipos basicos
- print/input y conversiones cuando corresponda
- lecturas simuladas de sensores y reportes

Instrucciones:
Crea una variable `temperatura`. Luego crea una variable booleana `lectura_valida` que sea `True` si la temperatura esta entre -40 y 80 grados, incluyendo los bordes. Imprime el resultado.

Ejemplo de entrada:
No uses input. Usa una temperatura fija.

Ejemplo de salida:
Lectura valida: True

Restricciones:
- Debes definir `temperatura` y `lectura_valida`. Usa una comparacion encadenada como `-40 <= temperatura <= 80`.
- No mirar la solucion antes de intentar.
- Mantener nombres de variables si el test los necesita.

Pistas:
1. Una comparacion produce `True` o `False`.
2. Python permite comparaciones encadenadas.
3. Prueba cambiando la temperatura a 90 para ver un caso invalido.

Reto extra:
Crea tambien una validacion para humedad entre 0 y 100.
"""

# =========================
# ZONA DE TRABAJO
# =========================
# Escribe tu codigo aqui
temperatura = 90
lectura_valida = -40 <= temperatura <= 80
print(f"La lectura es valida de {temperatura}: {lectura_valida}")

