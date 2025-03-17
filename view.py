import flet as ft


class View:
    def __init__(self, page: ft.Page):
        self._page = page  #prende una pagina da fuori e la imposta come pagina interna
        self._controller = None

    def loadInterface(self):
        """in questo modo definiamo e carichiamo tutti i controlli dell'interfaccia
        :return
        """
        self._txtIn = ft.TextField(label="Inserisci testo")
        self._btnIN = ft.ElevatedButton(text="Aggiungi", on_click=self._controller.handleAggiungi)
        row = ft.Row([self._txtIn, self._btnIN])
        self._txtOut = ft.Text()

        self._page.add(row, self._txtOut)

    def setController(self, c):
        self._controller = c
