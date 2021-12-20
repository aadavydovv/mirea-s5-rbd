import tkinter as tk
from tkinter import ttk

from misc.constants import *
from misc.credentials import users
from misc.functions import make_label, make_button, pack_default
from windows.failed_login import WindowFailedLogin
from windows.home import WindowHome


class WindowLogin:

    def __init__(self):
        self.widget = tk.Tk()

        self.widget.configure(bg=BG, padx=16, pady=16)
        self.widget.resizable(False, False)

        pack_default(make_label('Вход', self.widget))

        make_label('Логин', self.widget, font_size=12).pack(padx=8, pady=4)
        entry_login = ttk.Entry(self.widget)
        entry_login.pack(padx=8, pady=8)
        make_label('Пароль', self.widget, font_size=12).pack(padx=8, pady=4)
        entry_password = ttk.Entry(self.widget, show='*')
        entry_password.pack(padx=8, pady=8)
        make_button('Войти', self.widget,
                    lambda event: self.check_credentials(entry_login.get(), entry_password.get())).pack(padx=8, pady=16)
        self.widget.bind('<Return>', lambda event: self.check_credentials(entry_login.get(), entry_password.get()))

    def check_credentials(self, login, password):
        if (login in users.keys()) and (users[login] == password):
            WindowHome(self.widget, login)
            self.widget.withdraw()
        else:
            WindowFailedLogin(self.widget)
