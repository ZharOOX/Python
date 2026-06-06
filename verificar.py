from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path


RAIZ = Path(__file__).resolve().parent

SEMANAS = {
    0: "00_preparacion",
    1: "01_python_basico",
    2: "02_condicionales",
    3: "03_bucles",
    4: "04_listas_tuplas",
    5: "05_diccionarios_json",
    6: "06_funciones",
    7: "07_errores_depuracion",
    8: "08_archivos_csv_json",
    9: "09_modulos_entornos",
    10: "10_poo_basica",
    11: "11_automatizacion_pc",
    12: "12_proyecto_python_puro",
    13: "13_sensores_simulados",
    14: "14_protocolos_estado",
    15: "15_micropython_setup_esp32",
    16: "16_gpio_led_boton",
    17: "17_pwm_adc_buzzer",
    18: "18_sensores_i2c_oled",
    19: "19_serial_pyserial",
    20: "20_protocolos_json_serial",
    21: "21_flet_basico",
    22: "22_flet_esp32_serial",
    23: "23_web_esp32_celular",
    24: "24_mqtt_proyecto_final",
}

TESTS_USUARIO_SEMANA_1 = {
    1: "test_ejercicio_01_variables_sensor",
    2: "test_ejercicio_02_reporte_sensor",
    3: "test_ejercicio_03_celsius_fahrenheit",
    4: "test_ejercicio_04_corriente_ley_ohm",
    5: "test_ejercicio_05_temperatura_input",
    6: "test_ejercicio_06_lectura_valida",
    7: "test_ejercicio_07_mensaje_alerta",
    8: "test_ejercicio_08_promedio_dos_sensores",
    9: "test_ejercicio_09_fstrings_dos_decimales",
    10: "test_ejercicio_10_corregir_tipos",
    11: "test_ejercicio_11_mini_reporte_ambiental",
    12: "test_ejercicio_12_sensor_simulado_calibrado",
    13: "test_ejercicio_13_configuracion_basica",
    14: "test_ejercicio_14_modificar_umbral",
    15: "test_ejercicio_15_diagnostico_basico",
}


def ejecutar(comando: list[str]) -> int:
    print("Ejecutando:", " ".join(comando))
    return subprocess.call(comando, cwd=RAIZ)


def titulo_ejercicio(ruta: Path) -> str:
    texto = ruta.read_text(encoding="utf-8", errors="replace")
    match = re.search(r'"""[\s\r\n]*(Ejercicio\s+\d+\s+-\s+.+)', texto)
    if match:
        return match.group(1).strip()
    return ruta.stem


def ayuda() -> None:
    print(
        """
Uso:
  python verificar.py lista
  python verificar.py ejercicios 1
  python verificar.py ejecutar 1 1
  python verificar.py semana 1
  python verificar.py ejercicio 1 1

Ejemplos:
  python verificar.py lista
  python verificar.py ejercicios 1
  python verificar.py ejecutar 1 1
  python verificar.py ejercicio 1 1
  python verificar.py semana 1

Notas:
  - Semana 1 corresponde a la carpeta 01_python_basico.
  - El corrector automatico directo de ejercicios de usuario existe por ahora para Semana 1.
"""
    )


def obtener_semana(valor: str) -> tuple[int, Path]:
    numero = int(valor)
    if numero not in SEMANAS:
        raise SystemExit(f"Semana no valida: {numero}")
    carpeta = RAIZ / SEMANAS[numero]
    if not carpeta.exists():
        raise SystemExit(f"No existe la carpeta: {carpeta}")
    return numero, carpeta


def listar_semanas() -> None:
    for numero, carpeta in SEMANAS.items():
        print(f"Semana {numero:02d}: {carpeta}")


def listar_ejercicios(numero_semana: str) -> None:
    _, carpeta = obtener_semana(numero_semana)
    ejercicios = sorted((carpeta / "ejercicios").glob("ejercicio_*.py"))
    for ruta in ejercicios:
        print(f"{ruta.name}: {titulo_ejercicio(ruta)}")


def ejecutar_ejercicio(numero_semana: str, numero_ejercicio: str) -> int:
    _, carpeta = obtener_semana(numero_semana)
    ruta = carpeta / "ejercicios" / f"ejercicio_{int(numero_ejercicio):02d}.py"
    if not ruta.exists():
        raise SystemExit(f"No existe el ejercicio: {ruta}")
    return ejecutar([sys.executable, str(ruta)])


def verificar_semana(numero_semana: str) -> int:
    numero, carpeta = obtener_semana(numero_semana)
    if numero == 1:
        test = carpeta / "tests" / "test_ejercicios_usuario_semana_01.py"
        return ejecutar([sys.executable, "-m", "pytest", str(test)])
    return ejecutar([sys.executable, "-m", "pytest", str(carpeta / "tests")])


def verificar_ejercicio(numero_semana: str, numero_ejercicio: str) -> int:
    numero, carpeta = obtener_semana(numero_semana)
    ejercicio = int(numero_ejercicio)
    if numero == 1:
        nombre_test = TESTS_USUARIO_SEMANA_1.get(ejercicio)
        if not nombre_test:
            raise SystemExit(f"No hay test de usuario para ejercicio {ejercicio}.")
        test = carpeta / "tests" / "test_ejercicios_usuario_semana_01.py"
        return ejecutar([sys.executable, "-m", "pytest", f"{test}::{nombre_test}"])

    test = carpeta / "tests" / f"test_ejercicio_{ejercicio:02d}.py"
    if not test.exists():
        raise SystemExit(
            "Esta semana todavia no tiene test directo para ese ejercicio."
        )
    return ejecutar([sys.executable, "-m", "pytest", str(test)])


def main() -> int:
    if len(sys.argv) < 2:
        ayuda()
        return 0

    comando = sys.argv[1].lower()

    if comando == "lista":
        listar_semanas()
        return 0
    if comando == "ejercicios" and len(sys.argv) == 3:
        listar_ejercicios(sys.argv[2])
        return 0
    if comando == "ejecutar" and len(sys.argv) == 4:
        return ejecutar_ejercicio(sys.argv[2], sys.argv[3])
    if comando == "semana" and len(sys.argv) == 3:
        return verificar_semana(sys.argv[2])
    if comando == "ejercicio" and len(sys.argv) == 4:
        return verificar_ejercicio(sys.argv[2], sys.argv[3])

    ayuda()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
