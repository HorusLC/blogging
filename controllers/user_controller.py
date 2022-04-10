from entity.blogger import Blogger
from entity.user_enums import Gender
from services.login_service import Login
from services.register_service import RegistrationService
from views.commands.register_user import RegisterUserCommand
from views.components.item_form import ItemForm


class UserController:
    def __init__(self, login_service: Login, reg_service: RegistrationService, view=None):
        self.view = view
        self.login_service = login_service
        self.reg_service = reg_service

    def show_reg_form(self):

        form = ItemForm(self.view, Blogger('', '', '', '', '', Gender.Male, '', '', '', [], '', '', ), RegisterUserCommand(self))

    def register_user(self,user):
        self.reg_service.register(user)
