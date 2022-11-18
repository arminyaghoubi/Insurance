from UserInterfaceLayer import *
from customtkinter import *
from Model.UserModel import *
from UserInterfaceLayer import BaseFormClass


class MainFormClass(BaseFormClass):
    def __init__(self, user: User):
        super().__init__("Main Form",600,300)
        self.user = user

    def addContents(self):
        userLabel=CTkLabel(self.Window,text=f"Hi {self.user.UserName}")
        userLabel.grid(row=0,column=0,pady=10,padx=10)

