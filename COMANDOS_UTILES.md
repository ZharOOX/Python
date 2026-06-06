# Comandos utiles

```bash
python -m venv .venv
pip install -r requirements.txt
python 01_python_basico/ejemplos/ejemplo_01_temperatura_promedio.py
pytest
pytest 01_python_basico/tests
flet run 21_flet_basico/interfaz/app.py
python -m serial.tools.list_ports
git status
git add .
git commit -m "avance del curso"
```

## Verificar ejercicios por numero

No necesitas memorizar nombres internos de tests.

```bash
python verificar.py lista
python verificar.py ejercicios 1
python verificar.py ejecutar 1 1
python verificar.py ejercicio 1 1
python verificar.py semana 1
```

Significado:

- `lista`: muestra que carpeta corresponde a cada semana.
- `ejercicios 1`: lista los ejercicios de Semana 1.
- `ejecutar 1 1`: ejecuta Semana 1, ejercicio 1.
- `ejercicio 1 1`: verifica Semana 1, ejercicio 1 con pytest.
- `semana 1`: verifica todos los ejercicios corregibles de Semana 1.
