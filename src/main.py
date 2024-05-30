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

class App:
    """
    The main application class
    """
    def __init__(self):
        """
        Initialise a new GUI application 
        """
        self.app = tk.Tk()

        # Set up the master grid
        self.app.rowconfigure(0, weight=1)
        self.app.columnconfigure(0, weight=1)

        self.__setup_window()

        # Create the menu bar
        self.menu_bar = MenuBar(self.app)

        # Create the equation entry
        self.equation_entry = EquationEntry(self.app, add_equation_function=self.add_equation)

        # Create the history
        self.history = History(self.app)
        self.history.scrollableFrame.interior
        

        self.equations = [] # The list of equations currently being stored in the history window

        # Create some test equations
        self.equations.append(Equation("1+1"))
        self.equations.append(Equation("2+2"))
        self.equations.append(Equation("3+3"))

        for i in range(len(self.equations)):
            self.equations[i].create_equation(self.history.scrollableFrame.interior, i, deleteFunction=self.remove_equation)

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
        equation.create_equation(self.history.scrollableFrame.interior, len(self.equations), deleteFunction=self.remove_equation)
        self.history.scrollableFrame._resize_interior(None)
        self.history.scrollableFrame._update_scroll_region(None)
        self.equations.append(equation)

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
        self.app.title("Printing Calculator - Jack Duignan")

        self.app.minsize(500, 250)
        self.app.geometry("500x250")

    def start (self):
        """
        Start the printing calculator app
        """
        self.app.mainloop()


myapp = App()

# start the program
myapp.start()