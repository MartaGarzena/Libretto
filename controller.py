from view import View


class Controller:
    def __init__(self, v: View):
        self._view = v #serev per collegare controller e view

    def handleAggiungi(self, e):
        strIN = self._view._txtIn.value
        if strIN == "":
            self._view._txtOut.value = "Errore, inserire un testo"
            self._view._page.update()
            return
        self._view._txtOut.value = strIN
        self._view._page.update()
