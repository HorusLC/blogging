from tkinter import *
from tkinter import ttk

from controllers.user_controller import UserController
from utils.view_settings import center_resize_window
from views.commands.show_reg import ShowRegistrationCommand


class MainView(ttk.Frame):
    def __init__(self, root, user_controller: UserController):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        self.user_controller = user_controller
        self.grid(column=0, row=0, sticky='NWES')
        self.show_registration_command = ShowRegistrationCommand(user_controller)
        buttons_frame = ttk.Frame(self, padding="20 10 20 10")
        buttons_frame.grid(column=0, row=1, sticky="nsew")
        self.add_button = ttk.Button(buttons_frame, text="Register", padding=10,
                                     command=self.show_registration_command)
        self.add_button.grid(column=1, row=0, sticky='NE', padx=40, pady=20)
