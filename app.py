import tkinter as tk
from handlers import *

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # GUI setup code goes here
        pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()