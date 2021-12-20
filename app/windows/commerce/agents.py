import tkinter as tk

import queries.agents as queries
from misc.constants import *
from misc.functions import make_label, make_button, get_table, setup_widget_size, pack_default
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue


class WindowAgents:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        label = make_label('Контрагенты', frame)
        pack_default(label)

        table_name = 'Kontragent'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowAgents, self.widget, root)

        pack_default(make_button('Найти по ИНН', self.widget,
                                 lambda event: WindowEnterValue(self.widget, queries.by_inn,
                                                                ResultModes.SINGLE, host_window=WindowAgents,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по табельному номеру ответственного сотрудника-менеджера',
                                 self.widget, lambda event: WindowEnterValue(self.widget, queries.by_employee_number,
                                                                             ResultModes.ENTRY_LIST,
                                                                             host_window=WindowAgents,
                                                                             prev_root=self.widget, base_root=root)))
