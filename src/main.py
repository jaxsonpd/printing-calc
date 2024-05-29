## @file main.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The main file for the printing calculator project

import tkinter as tk
from tkinter import ttk

from equation import Equation
from menu_bar import MenuBar
from equation_entry import EquationEntry
from history import History


## @class App
# @brief The main application class
class App(tk.Tk):
    ## @brief The constructor for the App class
    # @param self The object pointer
    def __init__(self):
        super().__init__()

        # Set up the master grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.__setup_window()

        # Create the menu bar
        self.menu_bar = MenuBar(self)

        # Create the equation entry
        self.equation_entry = EquationEntry(self, add_equation_function=self.add_equation)

        # Create the history
        self.history = History(self)
        

        self.equations = [] # The list of equations currently being stored in the history window

        # Create some test equations
        self.equations.append(Equation("1+1"))
        self.equations.append(Equation("2+2"))
        self.equations.append(Equation("3+3"))

        for i in range(len(self.equations)):
            self.equations[i].create_equation(self.history.scrollableFrame.interior, i, deleteFunction=self.remove_equation)

    ## @brief Add an equation to the history
    # @param self The object pointer
    # @param event The event object
    def add_equation(self, event):
        # Create new Equation and clear entry
        equation = Equation(self.equation_entry.ent_equation.get())
        self.equation_entry.ent_equation.delete(0, tk.END)

        # Add created equation to the gui
        equation.create_equation(self.history.scrollableFrame.interior, len(self.equations), deleteFunction=self.remove_equation)
        self.history.scrollableFrame._resize_interior(None)
        self.history.scrollableFrame._update_scroll_region(None)
        self.equations.append(equation)

    ## @brief Remove an equation from the history
    # @param self The object pointer
    # @param equation The equation to remove
    def remove_equation(self, equation: Equation):
        self.equations.remove(equation)
        print(equation)

    ## @brief Create the main window
    # @param self The object pointer
    def __setup_window(self):
        # Set up the window
        self.title("Printing Calculator - Jack Duignan")

        self.minsize(500, 250)
        self.geometry("500x250")


myapp = App()

# start the program
myapp.mainloop()