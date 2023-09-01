from tkinter import *
import platform
from os import environ
from tkinter import messagebox

def do_crazy_stuff():
    SYSTEM = platform.system().strip().upper()
    KEY = 'username' if SYSTEM == 'WINDOWS' else 'USER'
    c = 0
    while True:
        c += 1
        messagebox.showerror('ERROR', f'HAHAHAHA Try again {environ[KEY]}')
        if c == 10:
            break

if __name__ == '__main__':
    do_crazy_stuff()
