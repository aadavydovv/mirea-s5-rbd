import tkinter as tk

from misc.constants import *
from misc.functions import make_label, setup_widget_size, pack_default


class WindowOutdatedEntries:

    def __init__(self, root, outdated_entries, entry_type):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        self.widget.lift()
        self.widget.attributes("-topmost", True)
        self.widget.attributes("-topmost", False)

        setup_widget_size(self.widget, wh=True)

        if len(outdated_entries) == 1:
            by_number = 'под номером'
            ended = 'завершено'
        else:
            by_number = 'под номерами'
            ended = 'завершены'

        pack_default(make_label(f'{entry_type} {by_number} {str(outdated_entries)[1:-1]} - {ended}!', self.widget))
