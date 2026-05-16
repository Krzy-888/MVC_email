import tkinter as tk
from tkinter import ttk
import regex as re

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def save(self, email):
        try:
            self.model.email = email
            self.model.save()
            self.view.show_success(f'The email {email} saved!')
        except ValueError as error:
            self.view.show_error(error)
        
# TEST
# from model import Model
# from view import View
# root = tk.Tk()
# model = Model('ABC@mail.com')
# view = View(root)
# controller = Controller(model,view)
# view.set_controler(controller)
# view.pack()
# root.mainloop()