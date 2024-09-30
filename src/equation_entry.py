## @file equation_entry.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The equation entry GUI object class

import tkinter as tk
from tkinter import ttk

from configuration import Config
from utils import rgb_to_tk

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
        # Values for tracking previous equations
        self.prev_equations = list()
        self.prev_equation_idx = 0

        self.theme = Config.load_json("./src/theme.json")

        # Create the equation frame  
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.add_equation_function = add_equation_function

        # Create the equation widgets
        self.ent_equation = tk.Entry(self)
        self.ent_equation.focus_set()
        self.ent_equation.bind("<Return>", self.add_equation_CB)
        self.ent_equation.bind("<Up>", self.prev_equation_CB)
        self.ent_equation.bind("<Down>", self.fwd_equation_CB)
        self.ent_equation.grid(row=0, column=0, sticky="nsew")

        # Colour scheme
        self.ent_equation.config(background=rgb_to_tk(self.theme.colours.entry_background),
                                 foreground=rgb_to_tk(self.theme.colours.entry_text),
                                 relief="flat",
                                 insertbackground="white",
                                 highlightcolor="white",
                                 highlightthickness=0,
                                 insertwidth=1,
                                 font=(self.theme.font.family, self.theme.font.size))
                                 

    def add_equation_CB(self, event:tk.Event):
        """
        The callback from the equation entry box enter

        ### Params:
        event : tk.Event
         The unused event object
        """
        # Create new Equation and clear entry
        equation_str = self.ent_equation.get()
        if (len(equation_str) == 0):
            return
        
        self.ent_equation.delete(0, tk.END)

        if (len(self.prev_equations) > 4):
            self.prev_equations.pop(0)

        self.prev_equations.append(equation_str)
        self.prev_equation_idx = len(self.prev_equations)

        if (self.add_equation_function != None):
            self.add_equation_function(equation_str)



    def prev_equation_CB(self, event:tk.Event):
        """
        The callback from the equation entry box up arrow
        to recall the previous equation

        ### Params:
        event : tk.Event
         The unused event object
        """
        if (self.prev_equation_idx <= 0):
            self.prev_equation_idx = 0
            return
        
        self.prev_equation_idx -= 1

        self.ent_equation.delete(0, tk.END)
        self.ent_equation.insert(0, self.prev_equations[self.prev_equation_idx])

        print(self.prev_equations, self.prev_equation_idx)

    def fwd_equation_CB(self, event:tk.Event):
        """
        The callback from the equation entry box down arrow
        to recall the forward equation

        ### Params:
        event : tk.Event
         The unused event object
        """
        if (self.prev_equation_idx >= len(self.prev_equations)-1):
            self.prev_equation_idx = len(self.prev_equations)
            return
        
        self.prev_equation_idx += 1

        self.ent_equation.delete(0, tk.END)
        self.ent_equation.insert(0, self.prev_equations[self.prev_equation_idx])

        print(self.prev_equations, self.prev_equation_idx)
