import tkinter as tk
from misc.constants import *
from misc.functions import make_label, make_button, pack_default, pack_button
from windows.fund.collections import WindowCollections
from windows.fund.items import WindowItems


class WindowFundHome:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)
        self.widget.resizable(False, False)

        pack_default(make_label('Фонд', self.widget))

        pack_button(make_button('Коллекции', self.widget, lambda event: WindowCollections(self.widget)))
        pack_button(make_button('Предметы', self.widget, lambda event: WindowItems(self.widget)))
