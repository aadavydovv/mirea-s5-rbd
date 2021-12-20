import tkinter as tk

from misc.constants import *
from misc.functions import make_label, setup_widget_size, pack_default, get_table_name_from_query
from misc.mysql_client import MySQLClient
from objects.entry_list import EntryList


class WindowResultEntryList:

    def __init__(self, root, query, host_window, prev_root, base_root):
        self.widget = tk.Toplevel(root, bg=BG, padx=PAD_X, pady=PAD_Y)

        setup_widget_size(self.widget, wh=True, resizable=True, maxsize=True)

        pack_default(make_label('Результат', self.widget))

        with MySQLClient() as mysql_client:
            result_values = mysql_client.query(query, QueryModes.GET)

        if not result_values[1]:
            pack_default(make_label('Не найдено', self.widget, font_size=12))
        else:
            EntryList(self.widget, result_values[0], result_values[1],
                      get_table_name_from_query(query), None, is_result=True,
                      host_window=host_window, prev_root=prev_root, base_root=base_root)
