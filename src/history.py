## @file history.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The history portion implemented as a scrollable frame

import tkinter as tk
from tkinter import ttk

from configuration import Config

from utils import rgb_to_tk

from scrollable_frame import ScrollableFrame
from equation import Equation 


class History(ScrollableFrame):
    """
    This class displays the equations in a scrollable format.
    """
    def __init__(self, master: tk.Tk = None):
        """
        The constructor for the History class

        ### Params:
        master : tk.Tk
         The master frame for the history window to be placed inside of.
        
        ### Variables:
        inner : tk.Frame
         The inner frame to place things in

        equations : list 
         A list of Equation objects that are currently in displayed
         
        """
        # Setup the scrollable frame
        super().__init__(master)

        self.theme = Config.load_json("./src/theme.json")

        self.inner.config(background=rgb_to_tk(self.theme.colours.background))
        self.canvas.config(background=rgb_to_tk(self.theme.colours.background))

        # Allow the frame to resize
        self.inner.rowconfigure(0, weight=1)
        self.inner.columnconfigure(0, weight=1)

        ## The list of Equation objects displayed in the frame  
        self.equations : list[Equation] = list()

        # Create some test equations
        self.equations.append(Equation("# Question 1:"))
        self.equations.append(Equation("1+1"))
        self.equations.append(Equation("5*2"))
        self.equations.append(Equation("3+3**2+4"))

        for i in range(len(self.equations)):
            self.equations[i].create_equation(self.inner, delete_function=self.remove_equation)
            self.equations[i].frm_equation.grid(row=i, column=0, sticky="ew")
        

    def remove_equation(self, equation: Equation):
        """
        Remove an equation from the history frame called by the delete
        button in the Equation widget.

        ### Params:
        equation : Equation
        The equation to remove
        """
        index = self.equations.index(equation)
        self.equations.remove(equation)

        # Re initialise the lower equations with the new index one higher
        for i in range(index, len(self.equations)):
            self.equations[i].frm_equation.grid(row=i, column=0, sticky="ew")

