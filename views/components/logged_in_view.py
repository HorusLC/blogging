from functools import partial
from tkinter import ttk, Menu

from controllers.blog_controller import BlogController
from entity.blog import Blog
from services.blog_management import BlogManagementService
from views.commands.blog_commands import ShowAddBlogCommand
from views.components.blog_form import BlogForm


class LoggedInFrame(ttk.Frame):
    def __init__(self, container, show_add_command, add_blog_command, user):
        super().__init__(container)
        self.user = user
        self.show_add_command = show_add_command
        self.add_blog_command = add_blog_command
        # container.grid(column=0, row=0,sticky='NSEW')
        # self.blog_button = ttk.Button(text='Blogs')
        # self.blog_button.grid(column=0, row=0, sticky='NSEW')
        self.name_label = ttk.Label(text='Hello, ' + user.username)
        self.name_label.grid(column=0, row=0, sticky='NSEW')
        self.menubar = Menu(container, bg='lightblue')
        container['menu'] = self.menubar
        menu_blog = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_blog, label='Blog', underline=0)
        menu_blog.add_command(label='Add blog', command=partial(show_add_command,self.user,self.add_blog_command,self))
        self.tkraise()
