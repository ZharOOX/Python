# Ejercicio 02: Reporte de sensor

## Objetivo
Practicar reportes con texto y numeros usando variables y f-strings.

## Enunciado
Crea un reporte de un sensor simulado. Debes crear variables para `dispositivo`, `ubicacion`, `temperatura` y `humedad`. Despues imprime un reporte que muestre el nombre del dispositivo o sensor, la ubicacion, la temperatura y la humedad.

## Entrada esperada
No uses input. Usa valores fijos, por ejemplo dispositivo "ESP32_SIM", ubicacion "Santiago", temperatura 24.5 y humedad 60.

## Salida esperada
Dispositivo: ESP32_SIM
Ubicacion: Santiago
Temperatura: 24.5 C
Humedad: 60 %

## Restricciones
La salida debe mencionar temperatura, humedad y ubicacion. Tambien debe aparecer la palabra dispositivo o sensor.

## Pistas breves
1. No basta con una variable llamada `lectura`; separa temperatura y humedad.
2. Usa un `print()` por linea para que el reporte sea facil de leer.
3. Si pytest falla, revisa que en la salida aparezcan las palabras temperatura, humedad y ubicacion.

## Variante extra
Agrega una variable `voltaje` al reporte.
