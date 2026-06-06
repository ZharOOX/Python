# Teoria minima

Una variable guarda un valor para usarlo despues. En este curso vas a usar variables para representar lecturas de sensores, configuraciones, estados y mensajes.

```python
temperatura = 24.5
humedad = 60
sensor = "DHT22 simulado"
conectado = True
```

Tipos basicos:

- `int`: numero entero, por ejemplo `60`.
- `float`: numero decimal, por ejemplo `24.5`.
- `str`: texto, por ejemplo `"ESP32_SIM"`.
- `bool`: verdadero o falso, `True` o `False`.

Para mostrar datos se usa `print()`:

```python
print("Sistema iniciado")
print(f"Temperatura: {temperatura} C")
```

Para pedir datos al usuario se usa `input()`. Importante: `input()` siempre entrega texto. Si necesitas calcular, convierte el valor.

```python
temperatura = float(input("Temperatura C: "))
```

Operaciones frecuentes:

- Suma: `a + b`
- Resta: `a - b`
- Multiplicacion: `a * b`
- Division: `a / b`
- Promedio: `(a + b) / 2`
- Fahrenheit: `celsius * 9 / 5 + 32`
- Ley de Ohm: `corriente = voltaje / resistencia`

Regla de trabajo: primero escribe una version minima funcional con valores fijos. Luego agrega `input()`, validaciones o mejoras.
