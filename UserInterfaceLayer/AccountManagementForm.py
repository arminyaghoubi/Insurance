from BusinessLogicLayer import RoleBusinessLogic
from BusinessLogicLayer import PharmacyBusinessLogic
from BusinessLogicLayer import UserBusinessLogic
from customtkinter import *
from tkinter import messagebox as msg

from Model import Pharmacy, User


class UserManagementFormClass:
    def changeRole(self, *args):
        if self.rolesCombobox.get() == "Pharmacy":
            self.pharmacyNameLabel.grid(row=3, column=0, pady=10, padx=10)
            self.pharmacyNameEntry.grid(row=3, column=1, pady=10, padx=10)
            self.glnLabel.grid(row=4, column=0, pady=10, padx=10)
            self.glnEntry.grid(row=4, column=1, pady=10, padx=10)
            self.phoneLabel.grid(row=5, column=0, pady=10, padx=10)
            self.phoneEntry.grid(row=5, column=1, pady=10, padx=10)
            self.addressLabel.grid(row=6, column=0, pady=10, padx=10)
            self.addressEntry.grid(row=6, column=1, pady=10, padx=10)
            self.registerButton.grid(row=7, column=1, pady=10, padx=10)
        else:
            self.pharmacyNameLabel.grid_forget()
            self.pharmacyNameEntry.grid_forget()
            self.glnLabel.grid_forget()
            self.glnEntry.grid_forget()
            self.phoneLabel.grid_forget()
            self.phoneEntry.grid_forget()
            self.addressLabel.grid_forget()
            self.addressEntry.grid_forget()

    def registerButtonClick(self):
        insertedId = 0
        if self.rolesCombobox.get() == "Pharmacy":
            insertedId = PharmacyBusinessLogic().Insert(Pharmacy(self.userNameEntry.get(),
                                                                 self.passwordEntry.get(),
                                                                 self.rolesCombobox.get(),
                                                                 self.pharmacyNameEntry.get(),
                                                                 self.glnEntry.get(),
                                                                 self.addressEntry.get(),
                                                                 self.phoneEntry.get()))
        else:
            insertedId = UserBusinessLogic().Insert(User(self.userNameEntry.get(),
                                                         self.passwordEntry.get(),
                                                         self.rolesCombobox.get()))

        if insertedId != 0:
            msg.showinfo('Done!', f'Registration was done successfully. ID: {insertedId}')
        else:
            msg.showerror('Error', 'Registration has failed')

    def __init__(self, parent):
        self.Parent = parent

        self.userNameLabel = CTkLabel(master=self.Parent, text="User name: ")
        self.userNameLabel.grid(row=0, column=0, pady=10, padx=10)
        self.userNameEntry = CTkEntry(master=self.Parent, width=300, placeholder_text="Enter your username",
                                      justify="center")
        self.userNameEntry.grid(row=0, column=1, pady=10, padx=10)

        self.passwordLabel = CTkLabel(master=self.Parent, text="Password: ")
        self.passwordLabel.grid(row=1, column=0, pady=10, padx=10)
        self.passwordEntry = CTkEntry(master=self.Parent, width=300, placeholder_text="Enter your password",
                                      justify="center", show="*")
        self.passwordEntry.grid(row=1, column=1, pady=10, padx=10)

        self.roles = RoleBusinessLogic().getAll()
        self.roleLabel = CTkLabel(master=self.Parent, text="Role: ")
        self.roleLabel.grid(row=2, column=0, pady=10, padx=10)
        self.rolesCombobox = CTkComboBox(master=self.Parent,
                                         command=self.changeRole,
                                         width=300,
                                         values=self.roles)
        self.rolesCombobox.grid(row=2, column=1, pady=10, padx=20)

        self.pharmacyNameLabel = CTkLabel(master=self.Parent, text="Pharmacy Name: ")
        self.pharmacyNameEntry = CTkEntry(master=self.Parent, width=300, placeholder_text="Enter Pharmacy Name:",
                                          justify="center")

        self.glnLabel = CTkLabel(master=self.Parent, text="GLN: ")
        self.glnEntry = CTkEntry(master=self.Parent, width=300, placeholder_text="Enter GLN:",
                                 justify="center")

        self.phoneLabel = CTkLabel(master=self.Parent, text="Phone: ")
        self.phoneEntry = CTkEntry(master=self.Parent, width=300, placeholder_text="Enter Phone:",
                                   justify="center")

        self.addressLabel = CTkLabel(master=self.Parent, text="Address: ")
        self.addressEntry = CTkEntry(master=self.Parent, width=300, height=50, placeholder_text="Enter Address:",
                                     justify="center")

        self.registerButton = CTkButton(master=self.Parent, width=300, text="Register", border_width=2,
                                        command=self.registerButtonClick)
        self.registerButton.grid(row=3, column=1, pady=10, padx=10)
