from tkinter import *
from tkinter import ttk

from utils.view_settings import center_resize_window


class LoginForm(Toplevel):
    def __init__(self, parent, command):
        super().__init__(parent)
        self.parent = parent
        self.command = command
        self.frame = ttk.Frame(self, padding="30 30 30 30")
        self.title("Login")
        self.frame.grid(row=0, column=0, sticky=NSEW)
        center_resize_window(self, height=200, width=300)

        self.models = []
        self.types = []
        self.entries = []

        ttk.Label(self.frame, text='Email', justify=CENTER).grid(column=1, row=1, sticky=EW)
        ttk.Label(self.frame, text='Password', justify=CENTER).grid(column=1, row=2, sticky=EW, pady=10)
        email_model = StringVar()
        password_model = StringVar()
        email_entry = ttk.Entry(self.frame, textvariable=email_model, justify=LEFT)
        email_entry.grid(column=2, row=1, sticky=EW, padx=5)
        self.models.append(email_model)
        password_entry = ttk.Entry(self.frame, textvariable=password_model, justify=LEFT)
        password_entry.grid(column=2, row=2, sticky=EW, padx=5)
        self.models.append(password_model)
        self.login_button = ttk.Button(self.frame, text="Sign in", padding=10, command=self.signin)
        self.login_button.grid(column=1, row=3, sticky=NE, padx=30, pady=10, columnspan=3)

        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def signin(self):
        self.dismiss()
        credentials = (self.models[0].get(), self.models[1].get())
        self.command(credentials)

    def dismiss(self):
        self.grab_release()
        self.destroy()
