# Tests de Semana 1

Esta carpeta tiene dos tipos de pruebas:

- `test_ejercicio_XX.py`: comprueba que la solucion oficial del ejercicio ejecuta.
- `test_ejercicios_usuario_semana_01.py`: comprueba tus archivos en `../ejercicios/`.

## Comando recomendado

Para revisar tu avance real de Semana 1:

```powershell
python -m pytest 01_python_basico/tests/test_ejercicios_usuario_semana_01.py
```

Si un ejercicio esta vacio o incompleto, pytest debe fallar. Eso es normal: el mensaje de error indica que falta corregir.

Para revisar solo un ejercicio especifico:

```powershell
python -m pytest 01_python_basico/tests/test_ejercicios_usuario_semana_01.py::test_ejercicio_01_variables_sensor
```

## Importante

Estos tests no reemplazan entender el codigo. Sirven como una revision automatica minima:

- verifican que el archivo ejecuta
- verifican que imprime algo cuando corresponde
- verifican algunas variables esperadas
- verifican calculos basicos cuando se puede

Si pytest pasa, todavia debes leer tu codigo y explicar por que funciona.
