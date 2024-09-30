## 
#  @file main.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The main file for the printing calculator project

import tkinter as tk
from tkinter import ttk

from equation import Equation
from menu_bar import MenuBar
from equation_entry import EquationEntry
from history import History

class App(tk.Tk):
    """
    The main application class
    """
    def __init__(self):
        """
        Initialise a new GUI application 
        """
        super().__init__()

        # Set up the master grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.__setup_window()

        # Create the history
        self.history = History(self)
        self.history.grid(row=0, column=0, sticky="nsew")

        # Create the menu bar
        self.menu_bar = MenuBar(self, [self.history])

        # Create the equation entry
        self.equation_entry = EquationEntry(self, add_equation_function=self.add_equation)
        self.equation_entry.grid(row=1, column=0, sticky="nsew")

    def add_equation(self, equation_str):
        """
        Add a new equation to the history. Called by the equation entry.

        ### Params:
        equation_str
         The equation to add
        """
        equation = Equation(equation_str, self.history.assignments)

        # Add created equation to the gui
        equation.create_equation(self.history.inner, delete_function=self.history.remove_equation)
        equation.frm_equation.grid(row=len(self.history.equations), column=0, sticky="ew")

        self.history.equations.append(equation)

        self.update_idletasks()

        self.history.scroll("bottom")

        return True

    def __setup_window(self):
        """
        Create the main application window
        """
        # Set up the window
        self.title("Printing Calculator")

        self.minsize(500, 250)
        self.geometry("500x250")

    def start (self):
        """
        Start the printing calculator app
        """
        self.mainloop()


myapp = App()

# start the program
myapp.start()