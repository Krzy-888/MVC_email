from tkinter import ttk
import tkinter as tk

class View(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)

        # label
        self.label = ttk.Label(self,text='Email:')
        self.label.grid(row=1,column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)
        # sabe button
        self.save_button = ttk.Button(self,text='Save',command=self.save_button_clicked)
        self.save_button.grid(row=1,column=3,sticky=tk.W)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2,column=1,sticky=tk.W)

        # controller
        self.controller = None

    def set_controler(self, controler):
        self.controller = controler
    
    def save_button_clicked(self):
        if self.controller:
            self.controller.save(self.email_var.get())
        
    def show_error(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000,self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000,self.hide_message)
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')
    
    def hide_message(self):
        self.message_label['text'] = ''

# TEST
# Sample data:
# ABC@mail.com
# ABC
# class testControler:
#     def __init__(self, view):
#         self.view = view
#     def save(self,value):
#         # simpler control version
#         if  '@' in value:
#             print(value)
#             self.view.show_success(f'The email {value} saved!')
#         else:
#             self.view.show_error('error')   
# root = tk.Tk()
# view = View(root)
# controller = testControler(view)
# view.set_controler(controller)
# view.pack()
# root.mainloop()