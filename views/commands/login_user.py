class ShowLoginCommand:
    def __init__(self, controller):
        self.user_controller = controller

    def __call__(self, *args, **kwargs):
        self.user_controller.show_login_form()


class LoginUserCommand:
    def __init__(self, controller):
        self.user_controller = controller

    def __call__(self, credentials):
        self.user_controller.login_user(credentials)
