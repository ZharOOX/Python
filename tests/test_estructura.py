from pathlib import Path


def test_semanas_existen():
    raiz = Path(__file__).resolve().parents[1]
    for numero in range(25):
        coincidencias = list(raiz.glob(f"{numero:02d}_*"))
        assert coincidencias, f"Falta semana {numero:02d}"
