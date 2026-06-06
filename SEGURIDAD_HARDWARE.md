# Seguridad de hardware

- El ESP32 usa logica de 3.3 V.
- No conectes 5 V directamente a un GPIO.
- Usa resistencias con LEDs.
- No alimentes motores desde el pin 3.3 V.
- Usa fuente externa para motores, servos o reles cuando corresponda.
- Conecta GND comun cuando una fuente externa deba compartir referencia con el ESP32.
- Ten cuidado con reles y corriente alterna.
- No manipules corriente alterna sin conocimientos adecuados.
- Revisa conexiones antes de energizar.
- Usa multimetro si es posible.
