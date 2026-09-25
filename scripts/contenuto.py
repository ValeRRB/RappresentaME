import customtkinter
from PIL import Image
from scripts.classe import FrameClasse
from scripts.azioni import FrameAzioni

class FrameContenuto(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=1)

        self.classe = FrameClasse(self, database)
        self.classe.grid(row=0, column=0, padx=8, pady=(8, 4), sticky="nsew")
        self.azioni = FrameAzioni(self, database)
        self.azioni.grid(row=1, column=0, padx=8, pady=(4, 8), sticky="nsew")
