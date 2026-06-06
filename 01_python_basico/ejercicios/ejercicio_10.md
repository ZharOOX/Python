# Ejercicio 10: Corregir tipos

## Objetivo
Practicar conversion de texto numerico a float antes de calcular.

## Enunciado
Simula una lectura que viene como texto, por ejemplo `lectura = "24.5"`. Crea `ajuste` como numero. Convierte `lectura` con `float()` y guarda la suma en `temperatura_corregida`. Imprime el resultado.

## Entrada esperada
No uses input. Usa una lectura de texto fija.

## Salida esperada
26.0

## Restricciones
Debes definir `temperatura_corregida` como numero. No sumes texto directamente con numero.

## Pistas breves
1. El problema es que `"24.5"` es texto.
2. Usa `float(lectura)` antes de sumar.
3. Si aparece TypeError, estas mezclando texto y numero.

## Variante extra
Cambia el ajuste y verifica el nuevo resultado.
