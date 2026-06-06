"""
Ejercicio 02 - Reporte de sensor

Objetivo:
Practicar reportes con texto y numeros usando variables y f-strings.

Conceptos:
- variables y tipos basicos
- print/input y conversiones cuando corresponda
- lecturas simuladas de sensores y reportes

Instrucciones:
Crea un reporte de un sensor simulado. Debes crear variables para `dispositivo`, `ubicacion`, `temperatura` y `humedad`. Despues imprime un reporte que muestre el nombre del dispositivo o sensor, la ubicacion, la temperatura y la humedad.

Ejemplo de entrada:
No uses input. Usa valores fijos, por ejemplo dispositivo "ESP32_SIM", ubicacion "Santiago", temperatura 24.5 y humedad 60.

Ejemplo de salida:
Dispositivo: ESP32_SIM
Ubicacion: Santiago
Temperatura: 24.5 C
Humedad: 60 %

Restricciones:
- La salida debe mencionar temperatura, humedad y ubicacion. Tambien debe aparecer la palabra dispositivo o sensor.
- No mirar la solucion antes de intentar.
- Mantener nombres de variables si el test los necesita.

Pistas:
1. No basta con una variable llamada `lectura`; separa temperatura y humedad.
2. Usa un `print()` por linea para que el reporte sea facil de leer.
3. Si pytest falla, revisa que en la salida aparezcan las palabras temperatura, humedad y ubicacion.

Reto extra:
Agrega una variable `voltaje` al reporte.
"""

# =========================
# ZONA DE TRABAJO
# =========================
# Escribe tu codigo aqui

nombre = 'microncontrolador'
ubicacion = 'santiago'
lectura = 50
temperatura = 24.5
voltaje = 3.3
humedad = 60
print(f"Sensor:{nombre} \nubicacion:{ubicacion} \nlecturas:(humedad:{humedad} Voltaje:{voltaje} Temperatura:{temperatura})")



