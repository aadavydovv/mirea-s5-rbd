import tkinter as tk

from misc.constants import *
from misc.functions import make_label, setup_widget_size, pack_default


class WindowFailedLogin:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)
        setup_widget_size(self.widget, wh=True)
        pack_default(make_label('Неправильный логин или пароль!', self.widget))
