import math
import re
import runpy
from pathlib import Path


RAIZ_SEMANA = Path(__file__).resolve().parents[1]
EJERCICIOS = RAIZ_SEMANA / "ejercicios"


def ejecutar(numero, capsys, monkeypatch, entrada="24.5"):
    monkeypatch.setattr("builtins.input", lambda mensaje="": entrada)
    ruta = EJERCICIOS / f"ejercicio_{numero:02d}.py"
    datos = runpy.run_path(str(ruta), run_name="__main__")
    salida = capsys.readouterr().out.strip()
    return datos, salida


def exigir_salida(salida, numero):
    assert salida, (
        f"El ejercicio {numero:02d} no imprimio nada. "
        "Agrega al menos un print() para mostrar el resultado."
    )


def exigir_numero(datos, nombre, numero):
    assert nombre in datos, (
        f"El ejercicio {numero:02d} debe definir la variable `{nombre}` "
        "para que pytest pueda revisarla."
    )
    assert isinstance(datos[nombre], (int, float)), (
        f"`{nombre}` debe ser un numero int o float."
    )


def salida_contiene(salida, *palabras):
    salida_normalizada = salida.lower()
    for palabra in palabras:
        assert palabra.lower() in salida_normalizada, (
            f"La salida debe mencionar `{palabra}`. Salida actual: {salida!r}"
        )


def test_ejercicio_01_variables_sensor(capsys, monkeypatch):
    datos, salida = ejecutar(1, capsys, monkeypatch)
    exigir_salida(salida, 1)
    for nombre in ("temperatura", "humedad", "voltaje"):
        exigir_numero(datos, nombre, 1)
    salida_contiene(salida, "temperatura", "humedad", "voltaje")


def test_ejercicio_02_reporte_sensor(capsys, monkeypatch):
    _, salida = ejecutar(2, capsys, monkeypatch)
    exigir_salida(salida, 2)
    salida_contiene(salida, "temperatura", "humedad")
    assert "dispositivo" in salida.lower() or "sensor" in salida.lower()
    assert "ubic" in salida.lower(), "La salida debe incluir ubicacion."


def test_ejercicio_03_celsius_fahrenheit(capsys, monkeypatch):
    datos, salida = ejecutar(3, capsys, monkeypatch)
    exigir_salida(salida, 3)
    exigir_numero(datos, "celsius", 3)
    exigir_numero(datos, "fahrenheit", 3)
    esperado = datos["celsius"] * 9 / 5 + 32
    assert math.isclose(datos["fahrenheit"], esperado), (
        "La formula debe ser fahrenheit = celsius * 9 / 5 + 32."
    )


def test_ejercicio_04_corriente_ley_ohm(capsys, monkeypatch):
    datos, salida = ejecutar(4, capsys, monkeypatch)
    exigir_salida(salida, 4)
    for nombre in ("voltaje", "resistencia", "corriente"):
        exigir_numero(datos, nombre, 4)
    assert datos["resistencia"] != 0, "La resistencia no puede ser cero."
    esperado = datos["voltaje"] / datos["resistencia"]
    assert math.isclose(datos["corriente"], esperado), (
        "La corriente debe calcularse como voltaje / resistencia."
    )


def test_ejercicio_05_temperatura_input(capsys, monkeypatch):
    datos, salida = ejecutar(5, capsys, monkeypatch, entrada="24.5")
    exigir_salida(salida, 5)
    exigir_numero(datos, "temperatura", 5)
    assert math.isclose(datos["temperatura"], 24.5), (
        "Convierte input() con float() y guarda el valor en `temperatura`."
    )


def test_ejercicio_06_lectura_valida(capsys, monkeypatch):
    datos, salida = ejecutar(6, capsys, monkeypatch)
    exigir_salida(salida, 6)
    exigir_numero(datos, "temperatura", 6)
    assert "lectura_valida" in datos, "Define `lectura_valida`."
    assert isinstance(datos["lectura_valida"], bool), "`lectura_valida` debe ser bool."
    assert datos["lectura_valida"] == (-40 <= datos["temperatura"] <= 80)


def test_ejercicio_07_mensaje_alerta(capsys, monkeypatch):
    datos, salida = ejecutar(7, capsys, monkeypatch)
    exigir_salida(salida, 7)
    assert "mensaje" in datos, "Crea una variable `mensaje` con el texto de alerta."
    assert isinstance(datos["mensaje"], str)
    salida_contiene(salida, "temperatura", "umbral")


def test_ejercicio_08_promedio_dos_sensores(capsys, monkeypatch):
    datos, salida = ejecutar(8, capsys, monkeypatch)
    exigir_salida(salida, 8)
    exigir_numero(datos, "promedio", 8)
    salida_contiene(salida, "promedio")
    if "sensor_1" in datos and "sensor_2" in datos:
        esperado = (datos["sensor_1"] + datos["sensor_2"]) / 2
        assert math.isclose(datos["promedio"], esperado)


def test_ejercicio_09_fstrings_dos_decimales(capsys, monkeypatch):
    datos, salida = ejecutar(9, capsys, monkeypatch)
    exigir_salida(salida, 9)
    exigir_numero(datos, "voltaje", 9)
    assert re.search(r"\d+\.\d{2}", salida), (
        "La salida debe mostrar un numero con dos decimales, por ejemplo 3.28."
    )


def test_ejercicio_10_corregir_tipos(capsys, monkeypatch):
    datos, salida = ejecutar(10, capsys, monkeypatch)
    exigir_salida(salida, 10)
    assert "temperatura_corregida" in datos, (
        "Guarda el resultado en `temperatura_corregida`."
    )
    assert isinstance(datos["temperatura_corregida"], (int, float))


def test_ejercicio_11_mini_reporte_ambiental(capsys, monkeypatch):
    _, salida = ejecutar(11, capsys, monkeypatch)
    exigir_salida(salida, 11)
    salida_contiene(salida, "temperatura", "humedad", "voltaje", "estado")


def test_ejercicio_12_sensor_simulado_calibrado(capsys, monkeypatch):
    datos, salida = ejecutar(12, capsys, monkeypatch)
    exigir_salida(salida, 12)
    for nombre in ("lectura_sensor", "offset", "lectura_calibrada"):
        exigir_numero(datos, nombre, 12)
    esperado = datos["lectura_sensor"] + datos["offset"]
    assert math.isclose(datos["lectura_calibrada"], esperado)


def test_ejercicio_13_configuracion_basica(capsys, monkeypatch):
    datos, salida = ejecutar(13, capsys, monkeypatch)
    exigir_salida(salida, 13)
    exigir_numero(datos, "intervalo_segundos", 13)
    exigir_numero(datos, "umbral_temperatura", 13)
    assert "modo" in datos, "Define la variable `modo`."
    assert isinstance(datos["modo"], str), "`modo` debe ser texto."


def test_ejercicio_14_modificar_umbral(capsys, monkeypatch):
    datos, salida = ejecutar(14, capsys, monkeypatch)
    exigir_salida(salida, 14)
    exigir_numero(datos, "temperatura", 14)
    exigir_numero(datos, "umbral", 14)
    salida_contiene(salida, "temperatura", "umbral")


def test_ejercicio_15_diagnostico_basico(capsys, monkeypatch):
    datos, salida = ejecutar(15, capsys, monkeypatch)
    exigir_salida(salida, 15)
    assert "nombre" in datos and isinstance(datos["nombre"], str)
    assert "version" in datos and isinstance(datos["version"], str)
    exigir_numero(datos, "voltaje", 15)
    assert "conectado" in datos and isinstance(datos["conectado"], bool)
    salida_contiene(salida, "voltaje", "conectado")
