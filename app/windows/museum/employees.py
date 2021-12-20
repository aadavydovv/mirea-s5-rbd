import tkinter as tk

import queries.employees as queries
from misc.constants import *
from misc.functions import make_label, make_button, get_table, setup_widget_size, pack_default, pack_button
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue
from windows.museum.passports import WindowPassports


class WindowEmployees:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        label = make_label('Сотрудники', frame)
        pack_default(label)

        table_name = 'Sotrudnik'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowEmployees, self.widget, root)

        pack_button(make_button('Паспортные данные', self.widget, lambda event: WindowPassports(self.widget)))

        frame_query_buttons = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        frame_query_buttons.pack(side=tk.BOTTOM)

        pack_default(make_button('Найти по табельному номеру', frame_query_buttons,
                                 lambda event: WindowEnterValue(self.widget, queries.by_number,
                                                                ResultModes.SINGLE, host_window=WindowEmployees,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти уволенных',
                                 frame_query_buttons, lambda event: WindowEnterValue(self.widget, queries.fired,
                                                                                     ResultModes.ENTRY_LIST,
                                                                                     host_window=WindowEmployees,
                                                                                     prev_root=self.widget,
                                                                                     base_root=root,
                                                                                     empty_query=True)))
        pack_default(make_button('Найти по ФИО', frame_query_buttons,
                                 lambda event: WindowEnterValue(self.widget, queries.by_fio,
                                                                ResultModes.ENTRY_LIST, host_window=WindowEmployees,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по должности', frame_query_buttons,
                                 lambda event: WindowEnterValue(self.widget, queries.by_position,
                                                                ResultModes.ENTRY_LIST, host_window=WindowEmployees,
                                                                prev_root=self.widget, base_root=root)))
