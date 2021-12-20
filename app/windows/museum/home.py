import tkinter as tk
from misc.constants import *
from misc.functions import make_label, make_button, pack_default, pack_button
from windows.museum.employees import WindowEmployees
from windows.museum.storages import WindowStorages


class WindowMuseum:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)
        self.widget.resizable(False, False)

        pack_default(make_label('Музей', self.widget))

        pack_button(make_button('Сотрудники', self.widget, lambda event: WindowEmployees(self.widget)))
        pack_button(make_button('Хранилища', self.widget, lambda event: WindowStorages(self.widget)))
