## 
# @file main.py
# @brief Main file for the printingCalc project
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk

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
    def __init__(self, master: tk.Widget = None):
        super().__init__(master)

        # Create the equation frame  
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.grid(row=1, column=0, sticky="nsew")

        # Create the equation widgets
        self.ent_equation = ttk.Entry(self)
        self.ent_equation.bind("<Return>", self.add_equation)
        self.ent_equation.grid(row=0, column=0, sticky="nsew")

        self.bind("<Return>", self.add_equation)

    ## @brief Add an equation to the history used by the equation entry
    # @param self The object pointer
    # @param event The event object
    def add_equation(self, event):
        pass

## @class History
# @brief The history class
class History(tk.Frame):
    ## @brief The constructor for the History class
    # @param self The object pointer
    # @param master The master widget to place the history in
    def __init__(self, master: tk.Widget = None):
        super().__init__(master)

        # Create the history frame
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky="nsew")

        # Create the history widgets
        self.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)

        self.equations = []

        # Add some equations to the history
        self.equations.append(Equation("2+2"))
        self.equations.append(Equation("2+3"))
        self.equations.append(Equation("2+4"))
        self.equations.append(Equation("2+5"))
        self.equations.append(Equation("2+6"))

        # Create the equations in the history
        for i in range(len(self.equations)):
            self.equations[i].create_equation(self, i, self.delete_equation)

    ## @brief Delete an equation from the history
    # @param self The object pointer
    # @param equation The equation object to delete
    def delete_equation(self, equation: Equation):
        self.equations.remove(equation)
        self.print_equations()
        
    ## @brief print the equations in the history
    # @param self The object pointer
    def print_equations(self):
        print("---")
        for equation in self.equations:
            print(equation)
        

## @class App
# @brief The main application class
class App(tk.Frame):
    ## @brief The constructor for the App class
    # @param self The object pointer
    # @param master The master widget to place the application in
    def __init__(self, master=None):
        super().__init__(master)

        self.setup_window()

        # Set up the master grid
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        # Create the menu bar
        self.menu_bar = MenuBar(self.master)

        # Create the equation entry
        self.equation_entry = EquationEntry(self.master)

        # Create the history
        self.history = History(self.master)

    ## @brief Create the main window
    # @param self The object pointer
    def setup_window(self):
        # Set up the window
        self.master.title("Printing Calculator - Jack Duignan")

        self.master.minsize(500, 250)
        self.master.geometry("500x250")

myapp = App()

# start the program
myapp.mainloop()