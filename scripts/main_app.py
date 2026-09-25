import customtkinter
from PIL import Image
from scripts.listaStudenti import FrameListaStudenti
from scripts.contenuto import FrameContenuto

class Main_Frame(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)
        self.rowconfigure(0, weight=1)

        self.listaStudenti = FrameListaStudenti(self, self.database)
        self.listaStudenti.grid(row=0, column=0, padx=(8,4), pady=8, sticky="nsew")
        self.contenuto = FrameContenuto(self, self.database)
        self.contenuto.grid(row=0, column=1, padx=(4, 8), pady=8, sticky="nsew")