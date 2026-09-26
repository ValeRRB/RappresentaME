import customtkinter
from PIL import Image
from utils import resource_path
from scripts.studente import FrameStudente

class FrameListaStudenti(customtkinter.CTkScrollableFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        #self.frames_studente = []

    #def aggiorna(self):
    #    for frame in self.frames_studenti:
    #        frame.destroy()
    #    self.frames_studenti.clear()

        self.prova = FrameStudente(self, 1, self.database)
        self.prova.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")