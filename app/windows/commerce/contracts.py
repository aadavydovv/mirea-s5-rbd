import datetime
import tkinter as tk

import queries.contracts as queries
from misc.constants import *
from misc.functions import make_label, make_button, get_table, setup_widget_size, pack_default
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue
from windows.outdated_entries import WindowOutdatedEntries


class WindowContracts:

    def __init__(self, root):
        self.root = root
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        label = make_label('Договоры', frame)
        pack_default(label)

        table_name = 'Zakljuchenie_dogovora'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowContracts, self.widget, root)

        pack_default(make_button('Найти договор по номеру', self.widget,
                                 lambda event: WindowEnterValue(self.widget, queries.by_number,
                                                                ResultModes.SINGLE, host_window=WindowContracts,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по ИНН контрагента', self.widget,
                                 lambda event: WindowEnterValue(self.widget, queries.by_agent_inn,
                                                                ResultModes.ENTRY_LIST, host_window=WindowContracts,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по табельному номеру сотрудника-менеджера', self.widget,
                                 lambda event: WindowEnterValue(self.widget, queries.by_manager_number,
                                                                ResultModes.ENTRY_LIST, host_window=WindowContracts,
                                                                prev_root=self.widget, base_root=root)))

        self.print_outdated_contracts(entries)

    def print_outdated_contracts(self, entries):
        outdated_entry_ids = []

        for entry in entries:
            end_date: datetime.date = entry[5]
            if end_date < datetime.date.today():
                outdated_entry_ids.append(entry[0])

        if len(outdated_entry_ids) > 0:
            if len(outdated_entry_ids) == 1:
                entry_label = 'Договор'
            else:
                entry_label = 'Договоры'

            WindowOutdatedEntries(self.root, outdated_entry_ids, entry_label)
