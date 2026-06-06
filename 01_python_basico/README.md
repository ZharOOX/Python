# Semana 1: Python basico aplicado a sensores simulados

Tema: variables, tipos de datos, `print`, `input`, operaciones y logica basica orientada a sensores simulados.

En esta semana no necesitas hardware. Vas a simular lecturas de temperatura, humedad, voltaje y corriente usando valores fijos o datos ingresados por teclado.

## Orden de trabajo

1. Lee `objetivos.md`.
2. Lee `teoria_minima.md` y `conceptos_clave.md`.
3. Ejecuta los 5 ejemplos en `ejemplos/`.
4. Resuelve los 15 ejercicios en `ejercicios/`.
5. Usa `pistas/` solo si te bloqueas.
6. Revisa `soluciones/` despues de intentar resolver.
7. Ejecuta los tests con `pytest`.
8. Cierra con el mini-proyecto `mini_proyecto/simulador_temperatura_basico/`.

## Comandos utiles

Desde la raiz del curso:

```powershell
python 01_python_basico/ejemplos/ejemplo_01_temperatura_promedio.py
python 01_python_basico/ejercicios/ejercicio_01.py
python -m pytest 01_python_basico/tests
```

En macOS/Linux los comandos son iguales si el entorno virtual ya esta activado.

## Verificar tus ejercicios con pytest

Para revisar tu trabajo real de Semana 1:

```powershell
python -m pytest 01_python_basico/tests/test_ejercicios_usuario_semana_01.py
```

Si un ejercicio esta vacio, pytest fallara. Usa el mensaje de error como guia para corregir.

Tambien puedes usar el verificador simple:

```powershell
python verificar.py ejercicios 1
python verificar.py ejercicio 1 1
python verificar.py semana 1
```

## Resultado esperado

Al terminar debes poder escribir un programa pequeno que guarde lecturas simuladas, haga calculos simples, muestre reportes claros y use variables con nombres legibles.
## Flujo de ejercicios en PyCharm

Abre `ejercicios/ejercicio_XX.py` como archivo principal. El enunciado esta dentro del docstring inicial y el codigo se escribe en la `ZONA DE TRABAJO`. Los archivos `.md` quedan como respaldo o explicacion extendida; las soluciones siguen separadas en `soluciones/`.

