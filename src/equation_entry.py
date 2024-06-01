## @file equation_entry.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The equation entry GUI object class

import tkinter as tk
from tkinter import ttk


class EquationEntry():
    """
    The equation entry class which contains the GUI element to 
    enter the equation.
    """
    def __init__(self, master: ttk.Widget = None, row : int = 1, add_equation_function = None):
        """
        The constructor for the EquationEntry class

        ### Params:
        master : ttk.widget
         The master frame to place the equation in

        add_equation_function : function = None
         The function used when enter is pressed to add the equation
         to the GUI.
        
        ### Variables:
        outer : tk.Frame
         The outer frame of the equation entry
        """
        self.outer = tk.Frame(master)

        # Create the equation frame  
        self.outer.rowconfigure(0, weight=1)
        self.outer.columnconfigure(0, weight=1)

        self.outer.grid(row=row, column=0, sticky="nsew")
        self.add_equation_function = add_equation_function

        # Create the equation widgets
        self.ent_equation = ttk.Entry(self.outer)
        self.ent_equation.bind("<Return>", self.add_equation)
        self.ent_equation.grid(row=0, column=0, sticky="nsew")

    def __getattr__(self, name):
        """
        Pass through attributes to the outer frame if they dont exist
        in EquationEntry

        ### Params:
        name : 
         The name of the attribute that is being looked for.

        ### Returns:
        out : 
         The result of using name on the outer frame
        """
        return getattr(self.outer, name)

    def add_equation(self, event:tk.Event):
        """
        The callback from the equation entry box

        ### Params:
        event : tk.Event
         The unused event object
        """
        if self.add_equation_function != None:
            self.add_equation_function(event)