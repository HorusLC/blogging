import tkinter.messagebox

from Exceptions.usererror import EmailNotFoundError, IncorrectPasswordError, EmailExistsError, UsernameExistsError
from controllers.home_controller import HomeController
from entity.blogger import Blogger
from entity.user_enums import Gender
from services.login_service import Login
from services.register_service import RegistrationService
from views.commands.login_user import LoginUserCommand
from views.commands.register_user import RegisterUserCommand
from views.components.item_form import ItemForm
from views.components.logged_in_menu import LoggedInFrame
from views.components.login_form import LoginForm


class UserController:
    def __init__(self, login_service: Login, reg_service: RegistrationService, view=None):
        self.view = view
        self.login_service = login_service
        self.reg_service = reg_service

    def show_reg_form(self):
        form = ItemForm(self.view, Blogger('', '', '', '', '', Gender.Male, '', '', '', [], '', '', ),
                        RegisterUserCommand(self))

    def register_user(self, user):
        try:
            messages = self.reg_service.validate_user_data(user)
            if len(messages) == 0:
                self.reg_service.register(user)
                messages.append('Successful Registration!')
        except EmailExistsError as email_err:
            tkinter.messagebox.showerror(title='Error', message=str(email_err))
        except UsernameExistsError as username_err:
            tkinter.messagebox.showerror(title='Error', message=str(username_err))
        return messages

    def show_login_form(self):
        form = LoginForm(self.view, LoginUserCommand(self))

    def login_user(self, credentials):
        try:
            user = self.login_service.try_login_email(credentials[0], credentials[1])
            print('Hello - ', user.username)
        except EmailNotFoundError as mailnotfound:
            tkinter.messagebox.showerror(title='Error', message=str(mailnotfound))
        except IncorrectPasswordError as wrongpassword:
            tkinter.messagebox.showerror(title='Error', message=str(wrongpassword))
        else:
            # self.view.grid_forget()
            # tkinter.messagebox.showinfo(title='Login Successful', message=f'Hello {user.username}')
            parent = self.view.container
            self.view.destroy()
            home_contr = HomeController(view=LoggedInFrame(parent, command=None, user=user))
