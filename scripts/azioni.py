import customtkinter
from PIL import Image

class FrameAzioni(customtkinter.CTkFrame):
    def __init__(self, master, database):
        super().__init__(master)
        self.database = database