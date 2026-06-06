"""
Ejercicio 01 - Crear variables de sensor

Objetivo:
Practicar la creacion de variables numericas y mostrar un reporte basico.

Conceptos:
- variables y tipos basicos
- print/input y conversiones cuando corresponda
- lecturas simuladas de sensores y reportes

Instrucciones:
Crea tres variables llamadas `temperatura`, `humedad` y `voltaje`. Asigna valores numericos fijos. Luego imprime un reporte que mencione claramente temperatura, humedad y voltaje con sus unidades.

Ejemplo de entrada:
No uses input. Usa valores fijos, por ejemplo temperatura 24.5, humedad 58 y voltaje 3.3.

Ejemplo de salida:
Temperatura: 24.5 C
Humedad: 58 %
Voltaje: 3.3 V

Restricciones:
- Debes definir `temperatura`, `humedad` y `voltaje` como numeros. La salida debe mencionar esas tres palabras.
- No mirar la solucion antes de intentar.
- Mantener nombres de variables si el test los necesita.

Pistas:
1. Empieza creando una variable por cada lectura.
2. Usa `print()` o f-strings para mostrar cada dato.
3. Si pytest falla, revisa que los nombres de variables sean exactamente `temperatura`, `humedad` y `voltaje`.

Reto extra:
Cambia los valores y mejora el formato del reporte.
"""

# =========================
# ZONA DE TRABAJO
# =========================
temperatura = 25
voltaje  = 30
humedad  = 20
print(f"la temperatura:{temperatura}, el voltaje:{voltaje}, humedad:{humedad}")


