import enum
import tkinter.messagebox
from enum import Enum
from tkinter import *
from tkinter import ttk
from typing import Iterable

from entity.user_enums import Gender
from utils.view_settings import center_resize_window

DEFAULT_ENTRY_WIDTH_PX = 250


class ItemForm(Toplevel):
    def __init__(self, parent, item, command, edit=False):
        super().__init__(parent)
        self.parent = parent
        self.item = item
        self.command = command
        self.edit = edit

        self.frame = ttk.Frame(self, padding="30 30 30 30")
        self.title("Registration")
        self.frame.grid(row=0, column=0, sticky=NSEW)
        center_resize_window(self)

        self.models = []
        self.types = []
        self.entries = []
        self.keys = list(self.item.__dict__.keys())
        for filter_field in ('id_', 'blogs_followed', 'role', '_module', '_class', 'last_login', 'date_reg', 'salt'):
            self.keys.remove(filter_field)
        self.columns = self.keys

        for i, col in enumerate(self.columns):
            # if col in ('id_', 'blogs_followed', 'role', '_module', '_class', 'last_login', 'date_reg', 'salt'):
            #     continue

            # add view models
            attr = getattr(self.item, col)
            if isinstance(attr, int):
                self.types.append("int")
            elif isinstance(attr, float):
                self.types.append("float")
            elif isinstance(attr, (tuple, list)):
                self.types.append("list")
            elif isinstance(attr, enum.Enum):
                self.types.append("Enum")
            else:
                self.types.append("str")
            model = StringVar()
            model.set(attr)
            self.models.append(model)

            # add labels
            title = col.title()
            if col == 'f_name':
                title = 'First Name'
            elif col == 'l_name':
                title = 'Last Name'
            ttk.Label(self.frame, text=title, justify=LEFT).grid(column=0, row=i, sticky=EW)

            # add entries
            if col == 'gender':

                model.set('1')
                r1 = Radiobutton(self.frame, text='Male', variable=model, value='1')
                r1.grid(column=1, row=i, sticky=W)
                r2 = Radiobutton(self.frame, text='Female', variable=model, value='2')
                r2.grid(column=1, row=i, sticky=W, padx=100)
            else:
                symbol_shown = None
                if col == 'password':
                    symbol_shown = '*'
                entry = ttk.Entry(self.frame, textvariable=model, show=symbol_shown)
                entry.grid(column=1, row=i, sticky=EW)
                self.entries.append(entry)

        # make form resizable
        rows, cols = self.frame.grid_size()
        for row in range(rows):
            self.frame.rowconfigure(row, weight=1)
        self.frame.columnconfigure(0, weight=1, minsize=DEFAULT_ENTRY_WIDTH_PX)
        self.frame.columnconfigure(1, weight=1, minsize=DEFAULT_ENTRY_WIDTH_PX)

        # add buttons
        buttons_frame = ttk.Frame(self.frame, padding="20 10 20 10")
        buttons_frame.grid(column=0, row=len(self.columns), columnspan=2, sticky=NSEW)

        self.reg_button = ttk.Button(buttons_frame, text="Register", padding=10, command=self.submit)
        self.reg_button.grid(column=1, row=0, sticky=NE, padx=40, pady=20)

        self.reset_button = ttk.Button(buttons_frame, text="Reset", padding=10, command=self.reset)
        self.reset_button.grid(column=2, row=0, sticky=NE, padx=40, pady=20)

        rows, cols = buttons_frame.grid_size()
        for col in range(cols):
            buttons_frame.columnconfigure(col, minsize=100, pad=30)

        # modal - capture visibility
        self.protocol("WM_DELETE_WINDOW", self.dismiss)
        self.transient(self.parent)
        self.wait_visibility()
        self.grab_set()
        self.wait_window()

    def submit(self):
        cls = type(self.item)
        result = cls()
        for i, col in enumerate(self.columns):
            str_val = self.models[i].get()
            if self.types[i] == "int":
                if col == 'gender':
                    value = Gender(int(str_val))
                else:
                    value = int(str_val)
            elif self.types[i] == "Enum":
                value = Gender(int(str_val))
            elif self.types[i] == "float":
                value = float(str_val)
            elif self.types[i] == "str":
                value = str_val
            elif self.types[i] == "list":
                value = [s.strip() for s in str_val.split(',')]
            setattr(result, col, value)
        print(self.command, result)
        messages = self.command(result)
        if len(messages) == 1 and messages[0] == 'Successful Registration!':
            tkinter.messagebox.showinfo(message=messages[0])
            self.dismiss()
        else:
            for msg in messages:
                tkinter.messagebox.showerror(title='Error!', message=msg)

    def reset(self):
        for i, col in enumerate(self.columns):
            attr = getattr(self.item, col)
            self.models[i].set(attr)

    def dismiss(self):
        self.grab_release()
        self.destroy()
