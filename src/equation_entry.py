## @file equation_entry.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The equation entry GUI object class

import tkinter as tk
from tkinter import ttk


class EquationEntry(tk.Frame):
    """
    The equation entry class which contains the GUI element to 
    enter the equation.
    """
    def __init__(self, master: tk.Widget = None, add_equation_function = None):
        """
        The constructor for the EquationEntry class

        ### Params:
        master : tk.Widget
         The master frame to place the equation in

        add_equation_function : function = None
         The function used when enter is pressed to add the equation
         to the GUI.
        
        ### Variables:
        outer : tk.Frame
         The outer frame of the equation entry
        """
        super().__init__(master)

        # Create the equation frame  
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.add_equation_function = add_equation_function

        # Create the equation widgets
        self.ent_equation = ttk.Entry(self)
        self.ent_equation.bind("<Return>", self.add_equation)
        self.ent_equation.grid(row=0, column=0, sticky="nsew")

    def add_equation(self, event:tk.Event):
        """
        The callback from the equation entry box

        ### Params:
        event : tk.Event
         The unused event object
        """
        if self.add_equation_function != None:
            self.add_equation_function(event)