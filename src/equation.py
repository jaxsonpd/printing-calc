## 
# @file equation.py
# @brief the Equation class for the printingCalc project
# @details This file contains the Equation class, which is used to store the equation its result and create the equation in the GUI
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk
from typing import Any

class Equation():
    """
    The equation class which stores the equation its result and contains
    the functions to display it in the GUI.
    """
    def __init__(self, equation: str):
        """
        Create an equation class

        ### Params:
        equation : str
         The raw equation string

        ### Variables:
        equation_str : str
         A string representation of the equation

        result : float or str
         The result of the equation

        frm_equation : str
         The outer frame of the equation
        """
        self.equation_str = equation
        self.result = self.__find_result()

    def __str__(self):
        """
        Return a string representation of the equation.

        ### Returns:
        out : str
        The equation in string format
        """
        return self.equation_str + " = " + str(self.result)
    
    def __find_result(self):
        """
        Find the result of an equation (should call a parsing function)
        but currently just uses the default python eval function.

        ### Returns:
        out : float or str
         The result of the equation, error if cannot be calculated
        """
        try:
            result = eval(self.equation_str)
        except:
            result = "error"
        
        return result
    
    def update_equation(self, equation: str):
        """
        Update the equation with new values essentially just a fancy
        setter. Currently doesn't update the GUI.

        ### Params:
        equation : str
         The new equation to update it with
        """
        self.equation_str = equation
        self.result = self.__find_result()
    
    def delete_equation(self, event: tk.Event = None):
        """
        Remove the equation from the GUI and call the outer delete
        function if provided. This is called from the delete button.

        ### Params:
        event : tk.Event
         The event object used when called from the button press. 
        """
        self.frm_equation.destroy() # Remove the equation from the GUI
        
        if self.delete_function != None:
            self.delete_function(self) # Remove the equation from the list

    def create_equation(self, master: tk.Widget, delete_function = None):
        """
        Create the equation GUI object. Currently places itself I 
        dont think that is the best way of doing it.

        ### Params:
        master : tk.Widget
         The master widget for the equation.
        delete_function = None
         The delete function to be called when the GUI object is destroyed.
        """
        # Create the equation frame
        self.frm_equation = tk.Frame(master)
        self.frm_equation.columnconfigure(0, weight=1)

        self.lbl_equation = ttk.Label(self.frm_equation, text=self.equation_str, anchor="w")
        self.lbl_equation.grid(row=0, column=0, sticky="new")
        self.lbl_answer = ttk.Label(self.frm_equation, text="="+str(self.result), anchor="w")
        self.lbl_answer.grid(row=1, column=0, sticky="new")
        
        self.btn_delete = ttk.Button(self.frm_equation, text="x", width=2, command=self.delete_equation)
        self.btn_delete.grid(row=0, column=1, rowspan=2, padx=10)

        # Set the delete function
        self.delete_function = delete_function


if __name__ == "__main__":
    equation1 = Equation("2+2")
    print(equation1)
    equation1.update_equation("2+3")
    print(equation1)

    equation1.create_equation(tk.Tk(), 0)
    tk.mainloop() # 2+3 \n =5
