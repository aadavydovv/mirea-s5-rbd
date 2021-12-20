import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

from misc.constants import *
from misc.functions import make_label, setup_widget_size, make_button
from misc.mysql_client import MySQLClient
from queries.misc import *


class WindowEntry:

    def __init__(self, root, initial_data, table_name, primary_key, field_names, prev_window, prev_root, base_root,
                 mode=ValuesWindowModes.EDIT, all_fields=False):
        self.base_root = base_root
        self.prev_root = prev_root
        self.prev_window = prev_window
        self.root = root
        self.mode = mode
        self.table_name = table_name
        self.primary_key = primary_key
        self.field_names = field_names
        self.values = initial_data[1]
        self.transliterated_field_names = initial_data[0]

        if mode == ValuesWindowModes.ADD:
            if not all_fields:
                self.values = self.values[1:]
                self.field_names = self.field_names[1:]
                self.transliterated_field_names = self.transliterated_field_names[1:]
            else:
                self.values = self.values
                self.field_names = self.field_names
                self.transliterated_field_names = self.transliterated_field_names

        self.widget = tk.Toplevel(root, bg=BG)

        setup_widget_size(self.widget, wh=2.0, maxsize=False)

        style = Style()
        style.configure('My.TFrame', background=BG)

        frame = ttk.Frame(self.widget, style='My.TFrame')
        canvas = tk.Canvas(frame)
        scroll = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)

        scrollable_frame = ttk.Frame(canvas, style='My.TFrame')
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox('all')
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scroll.set, bg=BG)

        frame.pack(fill=tk.BOTH)
        frame_buttons = ttk.Frame(self.widget, style='My.TFrame')
        frame_buttons.pack(side=tk.BOTTOM)
        make_button('Сохранить', frame_buttons, lambda e: self.save_values()).pack(side=tk.LEFT, padx=PAD_X, pady=PAD_Y)
        make_button('Отмена', frame_buttons, lambda e: self.widget.destroy()).pack(side=tk.LEFT, padx=PAD_X, pady=PAD_Y)

        canvas.pack(side='left', fill='both', expand=True)
        scroll.pack(side='right', fill='y')

        self.entry_widgets = []

        for n in range(len(self.transliterated_field_names)):
            entry_frame = ttk.Frame(scrollable_frame, style='My.TFrame')
            entry_frame.grid(column=0, row=n, sticky=tk.W, padx=PAD_X, pady=8)

            make_label(f'{self.transliterated_field_names[n]}', entry_frame, font_size=12).grid(column=0, row=0,
                                                                                                sticky=tk.W)

            entry = ttk.Entry(entry_frame)
            entry.grid(column=0, row=1, sticky=tk.W, pady=8)

            if any(self.values):
                formatted_value = self.values[n] if self.values[n] is not None else ''
                entry.insert(0, formatted_value)

            self.entry_widgets.append(entry)

    def save_values(self):
        actual_values = []

        for widget in self.entry_widgets:
            actual_values.append(widget.get())

        match self.mode:
            case ValuesWindowModes.ADD:
                query = add_entry_to_table(self.table_name, self.field_names, actual_values)
            case ValuesWindowModes.EDIT:
                query = update_entry_in_table(self.table_name, self.field_names, actual_values, self.primary_key,
                                              self.values[0])

        with MySQLClient() as mysql_client:
            mysql_client.query(query, QueryModes.EDIT)

        self.widget.destroy()
        self.prev_root.destroy()

        self.root.destroy()
        self.prev_window(self.base_root)
