## 
# @file main.py
# @brief Main file for the printingCalc project
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk
from typing import Any

from scrollableFrame import ScrollableFrame
from equation import Equation

## @class MenuBar
# @brief The menu bar class
class MenuBar(tk.Menu):
    ## @brief The constructor for the MenuBar class
    # @param self The object pointer
    # @param master The master widget to place the menu bar in
    def __init__(self, master: tk.Widget = None):
        super().__init__(master)

        # File menu
        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)

        # Add menus to the menu bar
        self.add_cascade(label="File", menu=filemenu)

        # Add the menu bar to the master
        self.master.config(menu=self)


## @class EquationEntry
# @brief The equation entry class
class EquationEntry(tk.Frame):
    ## @brief The constructor for the EquationEntry class
    # @param self The object pointer
    # @param master The master widget to place the equation entry in
    # @param row The row to place the equation entry in
    def __init__(self, master: tk.Widget = None, row: int = 1, add_equation_function = None):
        super().__init__(master)

        # Create the equation frame  
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.grid(row=row, column=0, sticky="nsew")
        self.add_equation_function = add_equation_function

        # Create the equation widgets
        self.ent_equation = ttk.Entry(self)
        self.ent_equation.bind("<Return>", self.add_equation)
        self.ent_equation.grid(row=0, column=0, sticky="nsew")


    ## @brief Add an equation to the history used by the equation entry
    # @param self The object pointer
    # @param event The event object
    def add_equation(self, event):
        if self.add_equation_function != None:
            self.add_equation_function(event)

## @class History
# @brief The history class
class History(ScrollableFrame):
    ## @brief The constructor for the History class
    # @param self The object pointer
    # @param master The master widget to place the history in
    def __init__(self, master: tk.Widget = None, row: int = 0):
        super().__init__(master)

        self.grid(row=row, column=0, sticky="nsew")
        self.frame = super().return_frame()

        # # Create the history frame
        # super().return_frame().rowconfigure(0, weight=1)
        # super().return_frame().columnconfigure(0, weight=1)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        return super().return_frame()



## @class App
# @brief The main application class
class App(tk.Frame):
    ## @brief The constructor for the App class
    # @param self The object pointer
    # @param master The master widget to place the application in
    def __init__(self, master=None):
        super().__init__(master)

        self.__setup_window()

        # Set up the master grid
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # Create the menu bar
        self.menu_bar = MenuBar(self.master)

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
            self.equations[i].create_equation(self.history.frame, i, deleteFunction=self.remove_equation)

    ## @brief Add an equation to the history
    # @param self The object pointer
    # @param event The event object
    def add_equation(self, event):
        equation = Equation(self.equation_entry.ent_equation.get())
        self.equation_entry.ent_equation.delete(0, tk.END)
        equation.create_equation(self.history, len(self.equations), deleteFunction=self.remove_equation)
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
        self.master.title("Printing Calculator - Jack Duignan")

        self.master.minsize(500, 250)
        self.master.geometry("500x250")



myapp = App()

# start the program
myapp.mainloop()