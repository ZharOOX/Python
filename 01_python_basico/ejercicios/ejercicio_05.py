"""
Ejercicio 05 - Temperatura por input

Objetivo:
Practicar entrada de usuario y conversion de texto a numero.

Conceptos:
- variables y tipos basicos
- print/input y conversiones cuando corresponda
- lecturas simuladas de sensores y reportes

Instrucciones:
Pide una temperatura al usuario con `input()`. Convierte el texto a numero con `float()` y guarda el resultado en una variable llamada `temperatura`. Imprime la lectura recibida.

Ejemplo de entrada:
24.5

Ejemplo de salida:
Lectura recibida: 24.5 C

Restricciones:
- Debes usar `float(input(...))` o una conversion equivalente. La variable final debe llamarse `temperatura`.
- No mirar la solucion antes de intentar.
- Mantener nombres de variables si el test los necesita.

Pistas:
1. Recuerda que `input()` devuelve texto.
2. Usa `float()` para poder trabajar con decimales.
3. Si pytest falla, revisa que la variable se llame exactamente `temperatura`.

Reto extra:
Pide tambien humedad y muestrala en el reporte.
"""

# =========================
# ZONA DE TRABAJO
# =========================
# Escribe tu codigo aqui

temperatura = float(input("Ingresa la temperatura: "))
print(f"La temperatura es: {temperatura}")
