class ShowAddBlogCommand:
    def __init__(self, controller, user):
        self.blog_controller = controller

    def __call__(self, user,delegate_command,view_container):
        self.blog_controller.show_blog_form(user,delegate_command,view_container)


class AddBlogCommand:
    def __init__(self, controller):
        self.controller = controller

    def __call__(self, blog, usr_id):
        self.controller.add_blog(blog, usr_id)
