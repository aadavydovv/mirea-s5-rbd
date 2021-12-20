import tkinter as tk

from misc.constants import *
from misc.functions import make_label, make_button, pack_default, pack_button
from windows.commerce.agents import WindowAgents
from windows.commerce.contracts import WindowContracts
from windows.commerce.nomenclature import WindowNomenclature
from windows.commerce.sales import WindowSales


class WindowCommerceHome:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)
        self.widget.resizable(False, False)

        pack_default(make_label('Коммерция', self.widget))

        pack_button(make_button('Договоры', self.widget, lambda event: WindowContracts(self.widget)))
        pack_button(make_button('Контрагенты', self.widget, lambda event: WindowAgents(self.widget)))
        pack_button(make_button('Номенклатурные позиции', self.widget, lambda event: WindowNomenclature(self.widget)))
        pack_button(make_button('Продажи билетов', self.widget, lambda event: WindowSales(self.widget)))
