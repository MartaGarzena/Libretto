import datetime

import flet as ft


class View:
    def __init__(self, page: ft.Page):
        self._student = None
        self._titolo = None
        self._txtOut = None
        self._btnIn = None
        self._txtIn = None
        self._controller = None
        self._page = page

    def loadInterface(self):
        """
        In questo metodo definiamo e carichiamo
        tutti i controlli dell'interfaccia.
        :return:
        """
        self._page.bgcolor = "white"
        self._titolo = ft.Text("Libretto Voti", color="red", size=24)
        self._student = ft.Text(self._controller.getStudent(), color="brown")
        row1 = ft.Row([self._titolo], alignment=ft.MainAxisAlignment.CENTER)
        row2 = ft.Row([self._student], alignment=ft.MainAxisAlignment.END)

        # riga dei controlli
        self._txtInNome=ft.TextField(label="nome esame ", hint_text="Inserisci il nome dell'esame", width=300)
        self._ddVoto=ft.Dropdown(label="voto", options=[], width=120)
        self._fillDDVoto() #remote fill drop

        self.dp = ft.DatePicker(
            first_date=datetime.datetime(2020, 1, 1),
            last_date=datetime.datetime(2025, 12, 31),
            on_change=lambda e: print(f"Giorno selezionato: {self.dp.value}"),
            on_dismiss=lambda e: print(f"Data non selezionata")
        )
        self_btnCal = ft.ElevatedButton("Pick date",icon=ft.icons.CALENDAR_MONTH, on_click=lambda _: self._page.open(self.dp))
        self._btnAdd= ft.ElevatedButton("Aggiungi",
                                        on_click=self._controller.handleAggiungi)
        self._btnPrint = ft.ElevatedButton("Stampa",
                                           on_click=self._controller.handleStampa)
        row3 = ft.Row([self._txtInNome, self._ddVoto, self_btnCal, self._btnAdd, self._btnPrint],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._txtOut = ft.ListView(expand=True)
        self._page.add(row1, row2, row3, self._txtOut)

    def setController(self, c):
        self._controller = c

    def _fillDDVoto(self):
        for i in range(18, 31):
            self._ddVoto.options.append(ft.dropdown.Option(str(i)))
        self._ddVoto.options.append(ft.dropdown.Option("30L"))
