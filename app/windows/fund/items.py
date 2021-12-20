import tkinter as tk

import queries.items as queries
from misc.constants import *
from misc.functions import make_label, make_button, get_table, setup_widget_size, pack_default
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue


class WindowItems:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        label = make_label('Музейные предметы', frame)
        pack_default(label)

        table_name = 'Muzejnyj_predmet'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowItems, self.widget, root)

        frame_buttons = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame_buttons)

        make_button('Найти по номеру коллекции', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.by_collection_number,
                                                   ResultModes.ENTRY_LIST, host_window=WindowItems,
                                                   prev_root=self.widget, base_root=root)).grid(column=0, row=0,
                                                                                                padx=PAD_X, pady=PAD_Y)
        make_button('Найти по наименованию', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.by_name,
                                                   ResultModes.ENTRY_LIST, host_window=WindowItems,
                                                   prev_root=self.widget, base_root=root)).grid(column=0, row=1,
                                                                                                padx=PAD_X, pady=PAD_Y)
        make_button('Найти по артикулу', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.by_code,
                                                   ResultModes.SINGLE, host_window=WindowItems,
                                                   prev_root=self.widget, base_root=root)).grid(column=0, row=2,
                                                                                                padx=PAD_X, pady=PAD_Y)

        make_button('Найти те, которые весят больше, чем N грамм', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.by_minimum_weight,
                                                   ResultModes.ENTRY_LIST, host_window=WindowItems,
                                                   prev_root=self.widget, base_root=root)).grid(column=1, row=0,
                                                                                                padx=PAD_X, pady=PAD_Y)
        make_button('Найти по периоду (годы)', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.by_period,
                                                   ResultModes.ENTRY_LIST, host_window=WindowItems,
                                                   prev_root=self.widget, base_root=root, period=True)).grid(column=1,
                                                                                                             row=1,
                                                                                                             padx=PAD_X,
                                                                                                             pady=PAD_Y)
        make_button('Найти те, у которых не указан год', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.without_year,
                                                   ResultModes.ENTRY_LIST, host_window=WindowItems,
                                                   prev_root=self.widget, base_root=root, empty_query=True)).grid(
            column=1, row=2,
            padx=PAD_X,
            pady=PAD_Y)
        make_button('Найти по типу', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.by_type,
                                                   ResultModes.ENTRY_LIST, host_window=WindowItems,
                                                   prev_root=self.widget, base_root=root)).grid(column=2, row=0,
                                                                                                padx=PAD_X, pady=PAD_Y)
