import runpy
from pathlib import Path


def test_solucion_ejercicio_03_ejecuta(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda mensaje="": "24.5")
    ruta = Path(__file__).resolve().parents[1] / "soluciones" / "ejercicio_03_solucion.py"
    runpy.run_path(str(ruta), run_name="__main__")
    salida = capsys.readouterr().out.strip()
    assert salida
