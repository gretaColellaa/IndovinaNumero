import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2025 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self._txtOutNMax = ft.TextField(label="N Max", disabled=True, width=200, value=self._controller.getNMax())
        self._txtOutTMax = ft.TextField(label="T Max", disabled=True, width=200, value=self._controller.getTMax())
        self._txtOutT = ft.TextField(label="T rimanenti", disabled=True, width=200)

        self._txtIn = ft.TextField(label="Tentativo",
                                   width=200,
                                   disabled=True) #creo il tasto disabilitato, si attiva se inizio la partita
        self._btnReset = ft.ElevatedButton(text="Nuova Partita",
                                           width=200,
                                           on_click=self._controller.reset)
        self._btnPlay = ft.ElevatedButton(text="Gioca",
                                          width=200,
                                          on_click=self._controller.play,
                                          disabled=True) #creo il tasto disabilitato, si attiva se inizio la partita

        self._lv = ft.ListView(expand=True)

        row1 = ft.Container(self._titolo, alignment=ft.alignment.center) #container del titolo
        # NOTA DIFFERENZA NELL'ALLIGNMENT !!!

        row2 = ft.Row([self._txtOutNMax, self._txtOutTMax, self._txtOutT],
                      alignment=ft.MainAxisAlignment.CENTER) #riga di tre elementi

        row3 = ft.Row([self._btnReset, self._txtIn, self._btnPlay],
                      alignment=ft.MainAxisAlignment.CENTER) #riga di tre elementi

        self._sl = ft.Slider(label="Difficoltà",
                             min=50, max=500,
                             value=100, width=600, divisions=10)
        self._sl.on_change = self._controller.setDifficulty

        self._pb = ft.ProgressBar(width=600, color="amber")



        self._page.add(row1, row2, self._sl, row3, self._pb, self._lv) #aggiungol elementi alla pagina

        self._page.update()

    def setController(self,controller):
        self._controller = controller

    def update(self):
        self._page.update()