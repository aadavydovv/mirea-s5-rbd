import tkinter as tk

import queries.events as queries
from misc.constants import *
from misc.functions import make_label, make_button, pack_default, pack_button, get_table, setup_widget_size
from objects.entry_list import EntryList
from windows.enter_value import WindowEnterValue
from windows.events.excursions import WindowExcursions
from windows.events.exhibitions import WindowExhibitions


class WindowEventsHome:

    def __init__(self, root):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=False)

        frame = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        pack_default(frame)

        pack_default(make_label('Мероприятия', frame))

        table_name = 'Meroprijatie'
        (fields, entries, original_column_names) = get_table(table_name, get_original_column_names=True)
        EntryList(frame, fields, entries, table_name, original_column_names, WindowEventsHome, self.widget, root)

        pack_button(make_button('Выставки', self.widget, lambda event: WindowExhibitions(self.widget)))
        pack_button(make_button('Экскурсии', self.widget, lambda event: WindowExcursions(self.widget)))

        frame_query_buttons = tk.Frame(self.widget, relief=tk.RAISED, background=BG)
        frame_query_buttons.pack(side=tk.BOTTOM)

        pack_default(make_button('Найти по номеру', frame_query_buttons,
                                 lambda event: WindowEnterValue(self.widget, queries.by_number,
                                                                ResultModes.SINGLE, host_window=WindowEventsHome,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по названию', frame_query_buttons,
                                 lambda event: WindowEnterValue(self.widget, queries.by_name,
                                                                ResultModes.ENTRY_LIST, host_window=WindowEventsHome,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по стандартной цене (менее чем...)', frame_query_buttons,
                                 lambda event: WindowEnterValue(self.widget, queries.by_standard_price_cap,
                                                                ResultModes.ENTRY_LIST, host_window=WindowEventsHome,
                                                                prev_root=self.widget, base_root=root)))
        pack_default(make_button('Найти по табельному номеру сотрудника-куратора', frame_query_buttons,
                                 lambda event: WindowEnterValue(self.widget, queries.by_curator_number,
                                                                ResultModes.ENTRY_LIST, host_window=WindowEventsHome,
                                                                prev_root=self.widget, base_root=root)))
