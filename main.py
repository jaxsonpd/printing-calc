## 
# @file main.py
# @brief Main file for the printingCalc project
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk

import equation

## @class App
# @brief The main application class
class App(tk.Frame):
    ## @brief The constructor for the App class
    # @param self The object pointer
    # @param master The master widget to place the application in
    def __init__(self, master=None):
        super().__init__(master)

        self.setup_window()

        self.setup_menuBar()

        # Set up the master grid
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)

        self.setup_history()

        self.create_equation_entry()

        # Add some equations to the history
        self.equations = []
        self.equations.append(equation.Equation("2+2"))
        self.equations.append(equation.Equation("2+3"))
        self.equations.append(equation.Equation("2+4"))
        self.equations.append(equation.Equation("2+5"))
        self.equations.append(equation.Equation("2+6"))

        # Create the equations in the history
        for i in range(len(self.equations)):
            self.equations[i].create_equation(self.frm_history, i)


    ## @brief Create the main window
    # @param self The object pointer
    def setup_window(self):
        # Set up the window
        self.master.title("Printing Calculator - Jack Duignan")

        self.master.minsize(500, 250)
        self.master.geometry("500x250")

    ## @brief Create the menu bar
    # @param self The object pointer
    def setup_menuBar(self):
        # Create the menu bar
        menuBar = tk.Menu(self.master)

        # File menu
        filemenu = tk.Menu(menuBar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)

        # Add menus to the menu bar
        menuBar.add_cascade(label="File", menu=filemenu)
        self.master.configure(menu=menuBar)

    ## @brief Setup the history frame
    # @param self The object pointer
    def setup_history(self):
        # Create the history frame
        self.frm_history = tk.Frame(self.master)
        self.frm_history.columnconfigure(0, weight=1)
        self.frm_history.grid(row=0, column=0, sticky="nsew")
        self.frm_history.rowconfigure(0, weight=1)

    ## @brief Create the equation entry widget
    # @param self The object pointer
    def create_equation_entry(self):
        # Create the equation frame  
        self.frm_equation = tk.Frame(self.master)
        self.frm_equation.rowconfigure(0, weight=1)
        self.frm_equation.columnconfigure(0, weight=1)

        self.frm_equation.grid(row=1, column=0, sticky="nsew")

        # Create the equation widgets
        self.ent_equation = tk.Entry(self.frm_equation)
        self.ent_equation.bind("<Return>", self.add_equation)
        self.ent_equation.grid(row=0, column=0, sticky="nsew")




myapp = App()

# start the program
myapp.mainloop()