from tkinter import ttk


class LoggedInFrame(ttk.Frame):
    def __init__(self, container, command, user):
        super().__init__(container)
        self.user = user
        self.command = command
        #container.grid(column=0, row=0,sticky='NSEW')
        #self.blog_button = ttk.Button(text='Blogs')
        #self.blog_button.grid(column=0, row=0, sticky='NSEW')
        self.name_label = ttk.Label(text='Hello, ' + user.username)
        self.name_label.grid(column=0, row=0, sticky='EW', padx=10)
        self.tkraise()
