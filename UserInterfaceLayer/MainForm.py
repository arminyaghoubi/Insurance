from customtkinter import *
from tkinter import *
from Model.UserModel import *
from UserInterfaceLayer import BaseFormClass
from UserInterfaceLayer.AccountManagementForm import UserManagementFormClass


class MainFormClass(BaseFormClass):
    def __init__(self, user: User):
        super().__init__("Main Form", 1000, 520)
        self.User = user

    def changeMode(self, mode):
        set_appearance_mode(mode)

    def hideAllFrames(self):
        self.frameRightAccount.grid_forget()

    def accountButtonClick(self):
        self.hideAllFrames()
        self.frameRightAccount.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

    def productButtonClick(self):
        self.hideAllFrames()

    def addContents(self):
        self.Window.grid_columnconfigure(1, weight=1)
        self.Window.grid_rowconfigure(0, weight=1)

        self.frameLeft = CTkFrame(master=self.Window,
                                  width=180,
                                  corner_radius=0)
        self.frameLeft.grid(row=0, column=0, sticky="nswe")

        self.frameRightAccount = CTkFrame(master=self.Window)
        self.frameRightAccount.grid_forget()
        UserManagementFormClass(self.frameRightAccount)

        self.frameLeft.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frameLeft.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frameLeft.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frameLeft.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.titleLabel = CTkLabel(master=self.frameLeft,
                                   text=f'Hi {self.User[1]}!',
                                   text_font=("Roboto Medium", -16))  # font name and size in px
        self.titleLabel.grid(row=0, column=0, pady=10, padx=10)

        # Admin==1
        if self.User[3] == 1:
            self.btnPharmacies = CTkButton(master=self.frameLeft,
                                           text="Accounts", command=self.accountButtonClick)
            self.btnPharmacies.grid(row=1, column=0, pady=10, padx=20)

            self.btnProducts = CTkButton(master=self.frameLeft,
                                         command=self.productButtonClick,
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
