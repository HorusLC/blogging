from tkinter import *

from utils.view_settings import center_resize_window

if __name__ == '__main__':
    root = Tk()
    center_resize_window(root, 800, 400)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.mainloop()
