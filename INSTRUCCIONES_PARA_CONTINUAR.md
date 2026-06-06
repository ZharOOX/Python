# Instrucciones para continuar desde Semana 2

Objetivo inmediato: continuar con `02_condicionales/` sin volver a explicar el curso completo.

## Contexto que debes mantener

- Curso practico en espanol.
- Separar siempre enunciados, pistas y soluciones.
- No poner soluciones dentro de los enunciados.
- Usar sensores simulados antes de hardware real.
- Mantener relacion con MicroPython, ESP32, Flet, web local e IoT.
- Priorizar versiones simples y funcionales antes de mejoras.

## Como continuar Semana 2

1. Abrir `02_condicionales/README.md`.
2. Revisar `objetivos.md`, `teoria_minima.md` y `conceptos_clave.md`.
3. Verificar que existan 5 ejemplos ejecutables sobre `if`, `elif`, `else`, comparaciones, alarmas y modos.
4. Completar o mejorar 15 ejercicios con esta distribucion:
   - 5 basicos
   - 5 intermedios
   - 3 aplicados a sensores, alarmas o comandos
   - 2 retos libres
5. Mantener cada ejercicio en:
   - `ejercicios/ejercicio_XX.py` como archivo principal autocontenido
   - `ejercicios/ejercicio_XX.md` como respaldo o explicacion extendida
   - `pistas/ejercicio_XX_pistas.md`
   - `soluciones/ejercicio_XX_solucion.py`
6. En cada `.py`, incluir docstring inicial con objetivo, instrucciones, entrada, salida, restricciones, pistas breves y `ZONA DE TRABAJO`.
7. Agregar o ajustar tests en `02_condicionales/tests/` cuando el ejercicio sea verificable.
8. Completar el mini-proyecto: sistema de alarma simulado por temperatura y humedad.
9. Ejecutar:

```powershell
python -m pytest 02_condicionales/tests
```

## Al terminar Semana 2

Actualizar `PLAN_DE_COMPLETADO.md` indicando que Semana 2 quedo revisada, probada y lista para estudio.
