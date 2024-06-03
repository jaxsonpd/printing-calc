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

        # Create the menu bar
        self.menu_bar = MenuBar(self)

        # Create the equation entry
        self.equation_entry = EquationEntry(self, add_equation_function=self.add_equation)
        self.equation_entry.grid(row=1, column=0, sticky="nsew")
        
        # Create the history
        self.history = History(self)
        self.history.grid(row=0, column=0, sticky="nsew")
        

        self.equations = [] # The list of equations currently being stored in the history window

        # Create some test equations
        self.equations.append(Equation("1+1"))
        self.equations.append(Equation("2+2"))
        self.equations.append(Equation("3+3"))

        for i in range(len(self.equations)):
            self.equations[i].create_equation(self.history.inner, delete_function=self.remove_equation)
            self.equations[i].frm_equation.grid(row=i, column=0, sticky="ew")

    def add_equation(self, event):
        """
        Add a new equation to the history. Called by the equation entry.

        ### Params:
        event : tk.event
         The event object as this is a callback (unused)
        """
        # Create new Equation and clear entry
        equation = Equation(self.equation_entry.ent_equation.get())
        self.equation_entry.ent_equation.delete(0, tk.END)

        # Add created equation to the gui
        equation.create_equation(self.history.inner, delete_function=self.remove_equation)
        equation.frm_equation.grid(row=len(self.equations), column=0, sticky="ew")

        self.equations.append(equation)

        self.update_idletasks()

        self.history.scroll("bottom")

    def remove_equation(self, equation: Equation):
        """
        Remove an equation from the history frame called by the delete
        button in the Equation widget.

        ### Params:
        equation : Equation
         The equation to remove
        """
        self.equations.remove(equation)
        print(equation)

    def __setup_window(self):
        """
        Create the main application window
        """
        # Set up the window
        self.title("Printing Calculator - Jack Duignan")

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