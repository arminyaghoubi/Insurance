from tkinter import messagebox as msg
from Model.UserModel import *
from customtkinter import *
from UserInterfaceLayer import *


class LoginFormClass(BaseFormClass):
    def __init__(self):
        super().__init__("Login Form")

    def loginButtonClick(self):
        user = User(self.userNameEntry.get(), self.passwordEntry.get())
        if user.UserName.lower() != "admin" or user.Password.lower() != "admin":
            msg.showerror("Error", "Username or password is incorrect")
        else:
            if self.rememberUserNameCheckBox.get():
                with open("UserPassData.csv", "w") as file:
                    print(user.UserName, user.Password, sep=",", file=file)

            self.Window.destroy()
            maniForm = MainFormClass(user)
            maniForm.load()
    def showPasswrodCheckBoxClick(self):
        if self.showPassword == "*":
            self.showPassword = ""
        else:
            self.showPassword = "*"
        self.passwordEntry.configure(show=self.showPassword)

    def getRememberMeData(self):
        if os.path.exists("UserPassData.csv"):
            with open("UserPassData.csv", "r") as file:
                line = file.readline()
                if line != "":
                    return line.split(",")

    def manageLoginButton(self, *args):
        if self.userNameEntry.get() != "" and self.passwordEntry.get() != "":
            self.loginButton.configure(state="normal")
        else:
            self.loginButton.configure(state="disabled")

    def addContents(self):
        self.userNameEntry = CTkEntry(master=self.Window, width=300, placeholder_text="Enter your username",
                                      justify="center")
        self.userNameEntry.bind("<KeyRelease>", self.manageLoginButton)
        self.userNameEntry.grid(row=0, column=0, pady=7, padx=50)

        self.showPassword = "*"
        self.passwordEntry = CTkEntry(master=self.Window, width=300, placeholder_text="Enter your password",
                                      justify="center", show=self.showPassword)
        self.passwordEntry.grid(row=1, column=0, pady=7, padx=0)
        self.passwordEntry.bind("<KeyRelease>", self.manageLoginButton)

        self.rememberUserNameCheckBox = CTkCheckBox(master=self.Window, text="remember me?")
        self.rememberUserNameCheckBox.grid(row=2, column=0, pady=7, padx=50, sticky="w")

        self.showPasswrodCheckBox = CTkCheckBox(master=self.Window, text="Show password",
                                                command=self.showPasswrodCheckBoxClick)
        self.showPasswrodCheckBox.grid(row=2, column=0, pady=7, padx=50, sticky="se")

        self.loginButton = CTkButton(master=self.Window, width=300, text="Login", border_width=2,
                                     command=self.loginButtonClick, state="disabled")
        self.loginButton.grid(row=3, column=0, pady=5, padx=50)

        user = self.getRememberMeData()
        if user is not None:
            self.userNameEntry.insert(0, user[0])
            self.passwordEntry.insert(0, user[1])
        self.manageLoginButton()
