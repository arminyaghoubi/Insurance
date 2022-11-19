import customtkinter
from abc import ABC, abstractmethod


class BaseFormClass(ABC):
    def __init__(self, title="", width=400, height=170, resizable=False, icon="favicon.ico"):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.Window = customtkinter.CTk()
        self.Window.title(title)
        positionRight = int(self.Window.winfo_screenwidth() / 2 - width / 2)
        positionDown = int(self.Window.winfo_screenheight() / 2 - height)
        self.Window.geometry(f"{width}x{height}+{positionRight}+{positionDown}")
        self.Window.iconbitmap(icon)
        if not resizable:
            self.Window.resizable(0, 0)

    @abstractmethod
    def addContents(self):
        pass

    def load(self):
        self.addContents()
        self.Window.mainloop()

    def closeForm(self):
        self.Window.destroy()