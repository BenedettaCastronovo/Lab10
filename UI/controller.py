import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._statoS = None

    def handleCalcola(self, e):
        self._anno = self._view._txtAnno.value
        if self._anno is None or self._anno == "":
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("inserire un valore"))
            self._view.update_page()
            return

        try:
            self._anno = int(self._anno)
        except:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("inserire un valore"))
            self._view.update_page()
            return

        self._model.creaGrafo(self._anno)
        mappaG = self._model.grado()
        self._view._txt_result.controls.clear()
        for k in mappaG:
            self._view._txt_result.controls.append(ft.Text(f" Stato {k} con grado {mappaG[k]}"))

        numCompC = self._model.getNumC()
        self._view._txt_result.controls.append(ft.Text(f"Numero: {numCompC}"))
        self._view._ddStato.options.clear()
        self.aggiungiStato()

        self._view.update_page()

    def aggiungiStato(self):
        for stato in self._model.getStati():
            self._view._ddStato.options.append(ft.dropdown.Option(
                key = stato.StateAbb,
                text = stato.StateAbb,
                data = stato,
                on_click = self._scelto))
        self._view.update_page()

    def _scelto(self, e):
        self._statoS = e.control.data

    def handleRaggiungi(self, e):
        if self._statoS is None:
            self._view._txt_result.controls.append("scegli stato")

        compC = self._model.getCompC(self._statoS)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Componente connessa dello stato selezionato: {self._statoS.StateAbb}"))
        for c in compC:
            self._view._txt_result.controls.append(ft.Text(f"Stato {c.StateAbb}")) #o nella dataclass str metto statename invece di code
        self._view.update_page()