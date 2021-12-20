import tkinter as tk
from misc.constants import *
from misc.functions import make_label, setup_widget_size, pack_default
from misc.mysql_client import MySQLClient


class WindowResultSingle:

    def __init__(self, root, query):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=True)

        pack_default(make_label('Результат', self.widget))

        with MySQLClient() as mysql_client:
            result_values = mysql_client.query(query, QueryModes.GET)

        if not result_values[1]:
            pack_default(make_label('Не найдено', self.widget, font_size=12))
        else:
            for n in range(len(result_values[0])):
                pack_default(make_label(f'{result_values[0][n]}: {result_values[1][0][n]}', self.widget, font_size=12))
