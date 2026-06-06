import flet as ft


def main(page: ft.Page):
    page.title = 'Dashboard de practica'
    page.add(ft.Text('Dashboard simulado'))


ft.app(target=main)
