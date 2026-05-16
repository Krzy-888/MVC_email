import tkinter as tk
from tkinter import ttk
import regex as re
from model import Model
from view import View
from controller import Controller

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo 2')
        app_model = Model()
        app_view = View(self)
        app_view.pack(padx=10,pady=10)
        app_controler = Controller(app_model,app_view)
        app_view.set_controler(app_controler)

if __name__ == '__main__':
    app = App()
    app.mainloop()