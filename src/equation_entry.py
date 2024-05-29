## @file equation_entry.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The equation entry GUI object class

import tkinter as tk
from tkinter import ttk


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