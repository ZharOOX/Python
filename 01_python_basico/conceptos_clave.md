# Conceptos clave

## Variable

Nombre que guarda un valor. Usa nombres descriptivos:

```python
temperatura_actual = 24.5
umbral_temperatura = 30
```

## Tipo de dato

El tipo define que puedes hacer con un valor. No es lo mismo `"24.5"` que `24.5`.

## Conversion

Convierte texto a numero cuando uses `input()`:

```python
lectura = float(input("Lectura: "))
```

## f-string

Permite crear mensajes claros:

```python
print(f"Voltaje: {voltaje:.2f} V")
```

## Sensor simulado

Un sensor simulado usa valores fijos o ingresados por teclado. Sirve para aprender logica antes de conectar hardware real.

## Umbral

Valor de referencia para comparar una lectura. En Semana 1 solo construiras mensajes o valores booleanos simples. En Semana 2 usaras `if`.

## Preguntas de control

1. Que variables necesita mi programa?
2. Que tipo tiene cada valor?
3. Necesito convertir texto a numero?
4. La salida se entiende sin leer el codigo?
5. Puedo cambiar el umbral sin reescribir todo?
