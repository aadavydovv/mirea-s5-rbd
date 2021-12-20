import tkinter as tk
from misc.constants import *
from misc.functions import make_label, make_button, get_table, setup_widget_size, pack_default
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue
import queries.sales as queries


class WindowSales:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        label = make_label('Продажи билетов', frame)
        pack_default(label)

        table_name = 'Prodazha_biletov'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowSales, self.widget, root)

        frame_buttons = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame_buttons)

        make_button('Найти по идентификатору', frame_buttons,
                    lambda event: WindowEnterValue(self.widget, queries.by_id,
                                                   ResultModes.SINGLE, host_window=WindowSales,
                                                   prev_root=self.widget, base_root=root)).grid(column=0, row=0,
                                                                                                padx=PAD_X, pady=PAD_Y)
        make_button('Найти по номеру мероприятия',
                    frame_buttons, lambda event: WindowEnterValue(self.widget, queries.by_event_number,
                                                                  ResultModes.ENTRY_LIST, host_window=WindowSales,
                                                                  prev_root=self.widget,
                                                                  base_root=root)).grid(column=0,
                                                                                        row=1,
                                                                                        padx=PAD_X,
                                                                                        pady=PAD_Y)
        make_button('Найти по временному периоду',
                    frame_buttons, lambda event: WindowEnterValue(self.widget, queries.by_period,
                                                                  ResultModes.ENTRY_LIST, host_window=WindowSales,
                                                                  prev_root=self.widget, base_root=root,
                                                                  period=True)).grid(column=0,
                                                                                     row=2,
                                                                                     padx=PAD_X,
                                                                                     pady=PAD_Y)
        make_button('Найти по дате посещения',
                    frame_buttons, lambda event: WindowEnterValue(self.widget, queries.by_visit_date,
                                                                  ResultModes.ENTRY_LIST, host_window=WindowSales,
                                                                  prev_root=self.widget,
                                                                  base_root=root)).grid(column=1,
                                                                                        row=0,
                                                                                        padx=PAD_X,
                                                                                        pady=PAD_Y)
        make_button('Найти по типу цены',
                    frame_buttons, lambda event: WindowEnterValue(self.widget, queries.by_price_type,
                                                                  ResultModes.ENTRY_LIST, host_window=WindowSales,
                                                                  prev_root=self.widget,
                                                                  base_root=root)).grid(column=1,
                                                                                        row=1,
                                                                                        padx=PAD_X,
                                                                                        pady=PAD_Y)
