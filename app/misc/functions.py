from tkinter import ttk
import tkinter as tk
import tkinter.font as tkfont
from misc.constants import *
from queries.misc import *
from misc.mysql_client import MySQLClient


# создание кнопки
def make_button(text, master, action=None, font_size=12):
    font = tkfont.Font(size=font_size)

    button = tk.Button(master, text=text, fg=FG,
                       bg=BUTTON_BG, highlightthickness=0, bd=0, font=font)

    if action:
        button.bind(LEFT_MOUSE_BUTTON, action)

    return button


# создание надписи
def make_label(text, master, font_size=18, anchor=tk.CENTER):
    font = tkfont.Font(size=font_size)
    return ttk.Label(master, text=text, foreground=FG, background=BG, font=font, anchor=anchor)


def get_table(table_name, get_original_column_names=False):
    with MySQLClient() as mysql_client:
        table = mysql_client.query(f"{SELECT_ALL_FROM} {table_name}", QueryModes.GET, get_original_column_names=get_original_column_names)
    return table


def setup_widget_size(widget, wh=True, resizable=False, maxsize=False):
    if not resizable:
        widget.resizable(False, False)

    # don't simplify
    if wh != True:
        if isinstance(wh, float):
            width = int(widget.winfo_screenwidth() / wh)
            height = int(widget.winfo_screenheight() / wh)
        else:
            width = int(widget.winfo_screenwidth() / 1.2)
            height = int(widget.winfo_screenheight() / 1.1)

        widget.minsize(width, 100)
        widget.maxsize(width, height)

    if maxsize:
        width = widget.winfo_screenwidth()
        height = widget.winfo_screenheight()
        widget.maxsize(int(width / 1.2), int(height / 1.1))


def pack_button(widget):
    widget.pack(padx=PAD_X, pady=PAD_Y, ipadx=PAD_X, ipady=PAD_Y, side=tk.LEFT)


def pack_default(widget):
    widget.pack(padx=PAD_X, pady=PAD_Y)


def get_table_name_from_query(query: str):
    return query.partition(' from ')[2].partition(' ')[0]
