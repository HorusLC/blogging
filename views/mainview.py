from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style

from controllers.user_controller import UserController
from utils.view_settings import center_resize_window
from views.commands.login_user import ShowLoginCommand
from views.commands.show_reg import ShowRegistrationCommand


class MainView(ttk.Frame):
    def __init__(self, root):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        # self.grid(column=0, row=0, sticky='NWES')
        self.pack()


        # Styles
