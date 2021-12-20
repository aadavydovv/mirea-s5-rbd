import tkinter as tk
from misc.constants import *
from misc.functions import make_label, make_button, get_table, setup_widget_size, pack_default
from objects.entry_list import EntryList


class WindowPassport:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        label = make_label('Паспорт', self.widget)
        pack_default(label)

        table_name = 'Pasportnye_dannye'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(self.widget, fields, entries, table_name, original_column_names)

        make_button('запрос', self.widget).pack(side=tk.LEFT, padx=16, pady=16)
