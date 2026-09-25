import customtkinter
from PIL import Image
from utils import resource_path

class FrameStudente(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database

        self.columnconfigure(0, weight=0, minsize=70)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

