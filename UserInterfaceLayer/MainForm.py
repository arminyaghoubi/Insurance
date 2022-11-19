from UserInterfaceLayer import *
from customtkinter import *
from Model.UserModel import *
from UserInterfaceLayer import BaseFormClass


class MainFormClass(BaseFormClass):
    def __init__(self, user: User):
        super().__init__("Main Form", 1000, 500)
        self.user = user

    def changeMode(self, mode):
        set_appearance_mode(mode)

    def addContents(self):
        self.Window.grid_columnconfigure(1, weight=1)
        self.Window.grid_rowconfigure(0, weight=1)

        self.frameLeft = CTkFrame(master=self.Window,
                                  width=180,
                                  corner_radius=0)
        self.frameLeft.grid(row=0, column=0, sticky="nswe")

        self.frame_right = CTkFrame(master=self.Window)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frameLeft.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frameLeft.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frameLeft.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frameLeft.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.titleLabel = CTkLabel(master=self.frameLeft,
                                   text="Insurance Application",
                                   text_font=("Roboto Medium", -16))  # font name and size in px
        self.titleLabel.grid(row=0, column=0, pady=10, padx=10)

        self.btnPharmacies = CTkButton(master=self.frameLeft,
                                       text="Pharmacies")
        self.btnPharmacies.grid(row=1, column=0, pady=10, padx=20)

        self.btnProducts = CTkButton(master=self.frameLeft,
                                     text="Products")
        self.btnProducts.grid(row=2, column=0, pady=10, padx=20)

        self.btnDoctores = CTkButton(master=self.frameLeft,
                                     text="Doctores")
        self.btnDoctores.grid(row=3, column=0, pady=10, padx=20)

        self.btnPatients = CTkButton(master=self.frameLeft,
                                     text="Patients")
        self.btnPatients.grid(row=4, column=0, pady=10, padx=20)

        self.optMode = CTkOptionMenu(master=self.frameLeft,
                                     values=["Dark", "Light", "System"],
                                     command=self.changeMode)
        self.optMode.grid(row=10, column=0, pady=10, padx=20, sticky="w")
