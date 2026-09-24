import customtkinter
from PIL import Image
from utils import resource_path
from database import Database
from scripts.listaStudenti import FrameListaStudenti

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("RappresentaME")
        self.geometry("1200x900")
        self.resizable(False, False)

        self.database = Database(r"db\database.db")
        
        customtkinter.set_appearance_mode("light")

if __name__ == "__main__":
    app = App()
    app.mainloop()