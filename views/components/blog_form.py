import tkinter.tix
from tkinter import ttk, StringVar, Toplevel

from entity.blog import Blog
from entity.blog_types import BlogCategory
from services.blog_management import BlogManagementService
from utils.view_settings import center_resize_window

DEFAULT_ENTRY_WIDTH_PX = 250


class BlogForm(Toplevel):
    def __init__(self, parent, item, command, user, edit=False):
        super().__init__(parent)
        self.parent = parent
        self.item = item
        self.command = command
        self.edit = edit
        self.user = user

        self.frame = ttk.Frame(self, padding="30 30 30 30")
        self.title("Add Blog")
        self.frame.grid(row=0, column=0, sticky='NSEW')
        center_resize_window(self)

        self.models = []
        self.types = []
        self.entries = []

        self.columns = tuple(self.item.__dict__.keys())

        ttk.Label(self.frame, text='Title', justify='left').grid(column=0, row=0, sticky='EW', pady=10)
        self.title = StringVar()
        title_entry = ttk.Entry(self.frame, textvariable=self.title)
        title_entry.grid(column=1, row=0, sticky='EW')

        ttk.Label(self.frame, text='Description', justify='left').grid(column=0, row=1, sticky='EW', pady=10)
        self.descr = StringVar()
        # descr_entry = ttk.Entry(self.frame, textvariable=self.descr)
        descr_frame = ttk.Frame(self.frame, width=30, height=5)
        descr_frame.grid(column=1, row=1)
        self.descr_entry = tkinter.Text(descr_frame, height=5, width=30)
        self.descr_entry.grid(column=0, row=0, sticky='EW')

        # ttk.Label(self.frame, text='Created', justify='left').grid(column=0, row=2, sticky='EW')
        # self.created= StringVar()
        # descr_entry = ttk.Entry(self.frame, textvariable=self.descr)
        # descr_entry.grid(column=1, row=1, sticky='EW')
        # ttk.Label(self.frame, text='Last Posted', justify='left').grid(column=0, row=3, sticky='EW')
        ttk.Label(self.frame, text='Tags(separated by ,)', justify='left').grid(column=0, row=2, sticky='EW', pady=10)
        self.tags = StringVar()
        tags_entry = ttk.Entry(self.frame, textvariable=self.tags)
        tags_entry.grid(column=1, row=2, sticky='EW')

        ttk.Label(self.frame, text='Category', justify='left').grid(column=0, row=3, sticky='W', pady=10)
        self.category = StringVar()
        options = [category.name for category in BlogCategory]
        option = ttk.OptionMenu(self.frame, self.category, options[2], *options)
        option.grid(column=1, row=3, sticky='W')

        # add labels

        # make form resizable
        rows, cols = self.frame.grid_size()
        for row in range(rows):
            self.frame.rowconfigure(row, weight=1)
        self.frame.columnconfigure(0, weight=1, minsize=DEFAULT_ENTRY_WIDTH_PX)
        self.frame.columnconfigure(1, weight=1, minsize=DEFAULT_ENTRY_WIDTH_PX)

        # add buttons
        self.add_button = ttk.Button(self.frame, text="Save", command=self.submit)
        self.add_button.grid(column=0, row=4, sticky='E', padx=20, pady=30)

        self.add_button = ttk.Button(self.frame, text="Reset", command=self.reset)
        self.add_button.grid(column=1, row=4, sticky='W', pady=30)

        # modal - capture visibility
        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def submit(self):
        blog = Blog(self.title.get(), self.descr_entry.get('1.0', 'end-1c'), None, None, self.tags.get(),
                    BlogCategory[self.category.get()])
        self.command(blog, self.user.id_)

    def reset(self):
        for i, col in enumerate(self.columns):
            attr = getattr(self.item, col)
            self.models[i].set(attr)

    def dismiss(self):
        self.grab_release()
        self.destroy()
