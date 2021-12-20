from misc.functions import make_label, make_button, pack_button, pack_default
import tkinter as tk
from misc.constants import *
from windows.commerce.home import WindowCommerceHome
from windows.fund.home import WindowFundHome
from windows.events.home import WindowEventsHome
from windows.museum.home import WindowMuseum
from misc.credentials import users


class WindowHome:

    def __init__(self, root, user):
        self.widget = tk.Toplevel(root, bg=BG, padx=16, pady=16)

        self.widget.configure(bg=BG, padx=16, pady=16)
        self.widget.resizable(False, False)

        pack_default(make_label('Информационная система музея', self.widget))

        usernames = list(users.keys())

        if user == usernames[0]:
            make_button('Коммерция', self.widget, lambda event: WindowCommerceHome(self.widget)).pack()
        elif user == usernames[1]:
            make_button('Мероприятия', self.widget, lambda event: WindowEventsHome(self.widget)).pack()
        elif user == usernames[2]:
            make_button('Фонд', self.widget, lambda event: WindowFundHome(self.widget)).pack()
        elif user == usernames[3]:
            make_button('Музей', self.widget, lambda event: WindowMuseum(self.widget)).pack()
        elif user == usernames[4]:
            pack_button(make_button('Коммерция', self.widget, lambda event: WindowCommerceHome(self.widget)))
            pack_button(make_button('Мероприятия', self.widget, lambda event: WindowEventsHome(self.widget)))
            pack_button(make_button('Фонд', self.widget, lambda event: WindowFundHome(self.widget)))
            pack_button(make_button('Музей', self.widget, lambda event: WindowMuseum(self.widget)))

