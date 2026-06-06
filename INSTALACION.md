# Instalacion

## Python y entorno virtual

Windows:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## PyCharm

Abre la carpeta `python-micropython-flet-iot-course/` como proyecto. Configura el interprete apuntando a `.venv`.

## Thonny y ESP32

Instala Thonny. En semanas 15 a 18 se explica como cargar firmware MicroPython, abrir REPL y usar `boot.py` y `main.py`.

## Prueba

```bash
python --version
pytest --version
```
