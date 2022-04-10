class RegisterUserCommand:
    def __init__(self, controller):
        self.controller = controller

    def __call__(self, user):
        return self.controller.register_user(user)
