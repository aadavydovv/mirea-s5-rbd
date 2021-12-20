import datetime
import tkinter as tk
from misc.constants import *
from misc.functions import make_label, make_button, setup_widget_size, pack_default, get_table
from misc.mysql_client import MySQLClient
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue
import queries.exhibitions as queries
from windows.outdated_entries import WindowOutdatedEntries


class WindowExhibitions:

    def __init__(self, root):
        self.root = root
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        label = make_label('Выставки', frame)
        pack_default(label)

        # table_name_0 = 'Meroprijatie'
        # table_name_1 = 'Vystavka'
        # query = f"select * from {table_name_0} " \
        #         f"inner join {table_name_1} V on {table_name_0}.Nomer_meroprijatija = V.Nomer_meroprijatija"
        # with MySQLClient() as mysql_client:
        #     table = mysql_client.query(query, QueryModes.GET, get_original_column_names=True)

        table_name = 'Vystavka'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowExhibitions, self.widget, root)

        pack_default(make_button('Получить период проведения по номеру выставки', self.widget,
                                 lambda event: WindowEnterValue(self.widget, queries.period_by_number,
                                                                ResultModes.SINGLE, host_window=WindowExhibitions,
                                                                prev_root=self.widget, base_root=root)))

        self.print_outdated_contracts(entries)

    def print_outdated_contracts(self, entries):
        outdated_entry_ids = []

        for entry in entries:
            end_date: datetime.date = entry[2]
            if end_date < datetime.date.today():
                outdated_entry_ids.append(entry[0])

        if len(outdated_entry_ids) > 0:
            if len(outdated_entry_ids) == 1:
                entry_label = 'Выставка'
            else:
                entry_label = 'Выставки'

            WindowOutdatedEntries(self.root, outdated_entry_ids, entry_label)
