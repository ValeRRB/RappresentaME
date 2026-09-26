import customtkinter
from PIL import Image
from utils import resource_path

class FrameStudente(customtkinter.CTkFrame):
    def __init__(self, master, studenteID, database):
        super().__init__(master)
        self.studenteID = studenteID
        self.database = database

        self.columnconfigure(0, weight=0, minsize=70)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.immagine_numero_studente = customtkinter.CTkImage(Image.open(resource_path(rf"assets\numeri\{self.studenteID}.png")),
                                                               size=(50, 50))
        self.label_numero_studente = customtkinter.CTkLabel(self,
                                                            image=self.immagine_numero_studente,
                                                            text=None)
        self.label_numero_studente.grid(row=0, column=0, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.fullName = self.database.get_fullName(self.studenteID)
        self.label_fullName = customtkinter.CTkLabel(self,
                                                     text=self.fullName,
                                                     font=("Arial", 24),
                                                     anchor="w")
        self.label_fullName.grid(row=0, column=1, padx=(0, 10), pady=(20, 0))

        self.email = self.database.get_email(self.studenteID)
        self.label_email = customtkinter.CTkLabel(self,
                                                  text=self.email,
                                                  font=("Arial", 16),
                                                  anchor="w")
        self.label_email.grid(row=1, column=1, padx=(0, 10), pady=10)