import tkinter as tk

import queries.excursions as queries
from misc.constants import *
from misc.functions import make_label, make_button, setup_widget_size, pack_default, get_table
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue


class WindowExcursions:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        label = make_label('Экскурсии', frame)
        pack_default(label)

        table_name = 'Ekskursija'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowExcursions, self.widget, root,
                  all_fields=True)

        pack_default(make_button('Найти по языку', self.widget,
                                 lambda event: WindowEnterValue(self.widget, queries.by_language,
                                                                ResultModes.ENTRY_LIST, host_window=WindowExcursions,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по максимальному количеству человек', self.widget,
                                 lambda event: WindowEnterValue(self.widget, queries.by_max_amount_of_participants,
                                                                ResultModes.ENTRY_LIST, host_window=WindowExcursions,
                                                                prev_root=self.widget, base_root=root)))
