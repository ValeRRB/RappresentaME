import customtkinter
from PIL import Image
from utils import resource_path
from database import Database
from scripts.main_app import Main_Frame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("RappresentaME")
        self.geometry("1200x900")
        self.resizable(False, False)

        self.database = Database(r"db\database.db")
        
        customtkinter.set_appearance_mode("light")

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.main_frame = Main_Frame(self, self.database)
        self.main_frame.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()