"""
Ejercicio 07 - Mensaje de alerta

Objetivo:
Practicar construccion de texto con variables.

Conceptos:
- variables y tipos basicos
- print/input y conversiones cuando corresponda
- lecturas simuladas de sensores y reportes

Instrucciones:
Crea `temperatura`, `umbral` y `mensaje`. El mensaje debe incluir la temperatura y el umbral. Imprime `mensaje`. No uses `if`; esta semana solo construimos el texto.

Ejemplo de entrada:
No uses input. Usa valores fijos.

Ejemplo de salida:
ALERTA posible: temperatura 31.2 C, umbral 30 C

Restricciones:
- Debes definir una variable llamada `mensaje`. La salida debe mencionar temperatura y umbral.
- No mirar la solucion antes de intentar.
- Mantener nombres de variables si el test los necesita.

Pistas:
1. Usa un f-string para insertar valores dentro del texto.
2. El mensaje puede decir alerta posible, sin decidir con if.
3. Si pytest falla, revisa que exista la variable `mensaje`.

Reto extra:
Agrega humedad al mensaje.
"""

# =========================
# ZONA DE TRABAJO
# =========================
# Escribe tu codigo aqui
temperatura = 40
umbral = 30
mensaje = "La temperatura es: " + str(temperatura) + "C y el umbral es:"  + str(umbral) + "C""

