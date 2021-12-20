import tkinter
from tkinter import ttk
from misc.constants import *
from misc.functions import make_button, pack_button
from misc.mysql_client import MySQLClient
from windows.entry import WindowEntry
from queries.misc import *
import tkinter as tk


class EntryList:

    def __init__(self, root, fields: tuple, entries: list, table_name, original_field_names, host_window, prev_root, base_root, is_result=False):
        self.base_root = base_root
        self.prev_root = prev_root
        self.host_window = host_window
        self.root = root
        self.entries = entries
        self.table_name = table_name
        self.fields = fields
        self.original_field_names = original_field_names

        with MySQLClient() as mysql_client:
            self.primary_key = mysql_client.query(primary_key_by_table(table_name), QueryModes.GET_PRIMARY_KEY)

        self.tv = ttk.Treeview(root, selectmode='browse')

        self.tv['columns'] = fields

        self.tv.column('#0', width=0, stretch=tkinter.NO)

        for field in fields:
            self.tv.column(field, anchor=tkinter.W)
            self.tv.heading(field, text=field, anchor=tkinter.W)

        for n in range(len(entries)):
            entries_n = tuple(x if x != None else '(не указано)' for x in entries[n])
            self.tv.insert(parent='', index=n, iid=n, text='', values=entries_n)

        self.tv.bind("<Double-1>", self.select)

        frame_buttons = tk.Frame(root, relief=tk.RAISED, background=BG)
        frame_buttons.pack(side=tkinter.RIGHT)

        scroll_v = ttk.Scrollbar(root, orient='vertical', command=self.tv.yview)
        scroll_v.pack(fill=tkinter.Y, side=tkinter.RIGHT)

        self.tv.pack(fill=tkinter.X)

        scroll_h = ttk.Scrollbar(root, orient='horizontal', command=self.tv.xview)
        scroll_h.pack(fill=tkinter.X)

        self.tv.configure(xscrollcommand=scroll_h.set, yscrollcommand=scroll_v.set)

        if not is_result:
            self.create_button_add(frame_buttons)
            self.create_button_remove(frame_buttons)

    def select(self, event):
        WindowEntry(self.root, (self.fields, self.entries[int(self.tv.selection()[0])]), self.table_name, self.primary_key, self.original_field_names, prev_window=self.host_window, prev_root=self.prev_root, base_root=self.base_root)

    def create_button_add(self, root):
        def open_add_entry_window():
            initial_data = (self.fields, [None] * len(self.fields))
            WindowEntry(self.root, initial_data, self.table_name, self.primary_key, self.original_field_names, mode=ValuesWindowModes.ADD, prev_window=self.host_window, prev_root=self.prev_root, base_root=self.base_root)

        make_button('Добавить', root, lambda e: open_add_entry_window()).pack(padx=PAD_X, pady=PAD_Y, ipadx=PAD_X, ipady=PAD_Y)

    def create_button_remove(self, root):
        def remove_entry():
            with MySQLClient() as mysql_client:
                mysql_client.query(delete_entry_from_table(self.table_name, self.primary_key, self.entries[int(self.tv.selection()[0])][0]), QueryModes.EDIT)

            self.update_values()

        make_button('Удалить выбранную запись', root, lambda e: remove_entry()).pack(padx=PAD_X, pady=PAD_Y, ipadx=PAD_X, ipady=PAD_Y)

    def update_values(self):
        self.tv.delete(self.tv.selection())
