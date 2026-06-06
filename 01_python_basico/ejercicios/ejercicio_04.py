"""
Ejercicio 04 - Corriente con Ley de Ohm

Objetivo:
Practicar division y variables relacionadas con electricidad basica.

Conceptos:
- variables y tipos basicos
- print/input y conversiones cuando corresponda
- lecturas simuladas de sensores y reportes

Instrucciones:
Crea `voltaje`, `resistencia` y `corriente`. Calcula la corriente con `corriente = voltaje / resistencia`. Imprime el resultado en amperes.

Ejemplo de entrada:
No uses input. Usa valores fijos, por ejemplo voltaje 5 y resistencia 1000.

Ejemplo de salida:
Corriente: 0.005 A

Restricciones:
- La resistencia no puede ser cero. Debes definir `voltaje`, `resistencia` y `corriente`.
- No mirar la solucion antes de intentar.
- Mantener nombres de variables si el test los necesita.

Pistas:
1. La formula es I = V / R.
2. Usa una resistencia positiva.
3. Si aparece division por cero, cambia el valor de resistencia.

Reto extra:
Calcula la corriente para una resistencia de 220 ohm.
"""

# =========================
# ZONA DE TRABAJO
# =========================
# Escribe tu codigo aqui

voltaje = 5
resistencia = 220
corriente = voltaje/resistencia

print(f"Con un voltaje de {voltaje} V y una resistencia de {resistencia} ohm, tenemos una corriente de {corriente} A")
