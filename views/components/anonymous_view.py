from tkinter import ttk
from tkinter.ttk import Style

from controllers.user_controller import UserController
from views.commands.login_user import ShowLoginCommand
from views.commands.show_reg import ShowRegistrationCommand


class AnonymousFrame(ttk.Frame):
    def __init__(self, container, controller: UserController):
        super().__init__(container)
        self.controller = controller
        self.show_registration_command = ShowRegistrationCommand(controller)
        self.show_login_command = ShowLoginCommand(controller)
        self.pack(anchor= 'center')
        # container.grid(column=0, row=0, sticky='NSEW')
        # btn_style = Style()
        # btn_style.theme_use('alt')
        # btn_style.configure('W.TButton', font=('Arial', 12, 'bold'), foreground='#75FF01', background='#50006C')
        # btn_style.map('W.TButton', background=[('active', '#75FF01')], foreground=[('active', '#50006C')])
        # buttons_frame = ttk.Frame(self, padding="20 10 20 10")
        self.register_button = ttk.Button(self, text="Register", padding=20,
                                          command=self.show_registration_command)
        self.register_button.grid(row=0,column=0)
        # self.register_button.grid(column=0, row=0)
        self.login_button = ttk.Button(self, text="Login", padding=20,
                                       command=self.show_login_command)
        self.login_button.grid(row=1,column=0)
        # self.login_button.grid(column=1, row=0)
        # buttons_frame.grid(column=0, row=0, sticky="nsew")

        self.tkraise()
