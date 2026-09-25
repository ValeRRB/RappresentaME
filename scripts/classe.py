import customtkinter
from PIL import Image

class FrameClasse(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database