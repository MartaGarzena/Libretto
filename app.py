import flet as ft

from controller import Controller
from view import View


def main(page: ft.Page):
    v = View()
    c = Controller(v)
    v.setController(c)
    v.loadInterface()


ft.app(target=main)
