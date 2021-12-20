import tkinter as tk
from tkinter import ttk

from misc.constants import *
from misc.functions import setup_widget_size, make_label, pack_default
from windows.result.entry_list import WindowResultEntryList
from windows.result.single import WindowResultSingle


class WindowEnterValue:

    def __init__(self, root, query, result_mode, host_window, prev_root, base_root, empty_query=False, period=False):
        if empty_query:
            match result_mode:
                case ResultModes.SINGLE:
                    WindowResultSingle(root, query())
                case ResultModes.ENTRY_LIST:
                    WindowResultEntryList(root, query(), host_window, prev_root, base_root)
            return

        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        setup_widget_size(self.widget, wh=True)

        pack_default(make_label('Введите значение', self.widget))

        entry = ttk.Entry(self.widget)
        pack_default(entry)

        if period:
            def format_period(unformatted_period: str):
                partitioned_period = unformatted_period.partition(', ')
                return partitioned_period[0], partitioned_period[2]

            match result_mode:
                case ResultModes.SINGLE:
                    self.widget.bind('<Return>',
                                     lambda event: WindowResultSingle(self.widget, query(format_period(entry.get()))))
                case ResultModes.ENTRY_LIST:
                    self.widget.bind('<Return>', lambda event: WindowResultEntryList(self.widget,
                                                                                     query(format_period(entry.get())),
                                                                                     host_window=host_window,
                                                                                     prev_root=prev_root,
                                                                                     base_root=base_root))
            return

        match result_mode:
            case ResultModes.SINGLE:
                self.widget.bind('<Return>', lambda event: WindowResultSingle(self.widget, query(entry.get())))
            case ResultModes.ENTRY_LIST:
                self.widget.bind('<Return>', lambda event: WindowResultEntryList(self.widget, query(entry.get()),
                                                                                 host_window=host_window,
                                                                                 prev_root=prev_root,
                                                                                 base_root=base_root))
