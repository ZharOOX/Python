# Solucion de problemas

## Python
- `SyntaxError`: revisa parentesis, comillas y dos puntos.
- `IndentationError`: revisa sangria consistente de 4 espacios.
- `NameError`: hay una variable mal escrita o no definida.
- `TypeError`: estas mezclando tipos incompatibles.

## PyCharm
- Si no encuentra paquetes, revisa el interprete configurado.
- Si ejecuta otro archivo, revisa la configuracion de Run.

## pip
- Actualiza pip con `python -m pip install --upgrade pip`.
- Activa el entorno virtual antes de instalar.

## Flet
- Si no abre ventana, prueba `flet run ruta/app.py`.
- Si falla importacion, instala requirements.

## pyserial
- Lista puertos con `python -m serial.tools.list_ports`.
- Cierra Thonny antes de abrir el puerto desde Python.

## ESP32 y MicroPython
- Verifica cable USB de datos.
- Revisa el puerto correcto.
- No conectes 5 V a GPIO.

## Wi-Fi y MQTT
- Verifica SSID, clave y red local.
- Asegura que PC y celular esten en la misma red para web local.
- Revisa direccion del broker y topics.
