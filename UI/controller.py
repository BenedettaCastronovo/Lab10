import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None

    def handleCalcola(self, e):
        self._anno = self._view._txtAnno.value
        if self._anno is None or self._anno == "":
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("inserire un valore"))

        try:
            self._anno = int(self._anno)
        except:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("inserire un valore"))
        self._view.update_page()

        self._model.creaGrafo(self._anno)
        mappaG = self._model.grado()
        self._view._txt_result.controls.clear()
        for k in mappaG:
            self._view._txt_result.controls.append(ft.Text(f" Stato {k} con grado {mappaG[k]}"))

        numCompC = self._model.getNumC()
        self._view._txt_result.controls.append(ft.Text(f"Numero: {numCompC}"))