# Ejercicio 09: Salida con f-strings

## Objetivo
Practicar formato de numeros decimales.

## Enunciado
Crea una variable `voltaje` con un decimal largo, por ejemplo 3.2789. Imprime el voltaje usando f-string con dos decimales: `{voltaje:.2f}`.

## Entrada esperada
No uses input. Usa un valor fijo para voltaje.

## Salida esperada
Voltaje: 3.28 V

## Restricciones
Debes definir `voltaje` como numero. La salida debe mostrar algun numero con exactamente dos decimales.

## Pistas breves
1. Dentro de un f-string puedes escribir `{voltaje:.2f}`.
2. El formato redondea visualmente el numero.
3. Si pytest falla, revisa que aparezcan dos digitos despues del punto.

## Variante extra
Muestra tambien corriente con tres decimales.
