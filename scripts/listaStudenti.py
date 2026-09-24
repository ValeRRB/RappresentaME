import customtkinter
from PIL import Image
from utils import resource_path

class FrameListaStudenti(customtkinter.CTkFrame):
    def __init__(self, database):
        super.__init__()
        self.database = database