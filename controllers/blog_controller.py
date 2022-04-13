from entity.blog import Blog
from services.blog_management import BlogManagementService
from views.commands.blog_commands import AddBlogCommand
from views.components.blog_form import BlogForm


class BlogController:
    def __init__(self, blog_service: BlogManagementService, view=None):
        self.view = view
        self.blog_service = blog_service

    def show_blog_form(self, usr, delegate_command,view_container):
        view = BlogForm(view_container, Blog('', '', '', '', '', '', '', ''), delegate_command, usr)

    def add_blog(self, blog, usr_id):
        self.blog_service.add_blog(blog, usr_id)
