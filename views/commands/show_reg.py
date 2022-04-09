class ShowRegistrationCommand:
    def __init__(self, controller):
        self.user_controller = controller

    def __call__(self, *args, **kwargs):
        self.user_controller.show_reg_form()
