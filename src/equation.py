## 
# @file equation.py
# @brief the Equation class for the printingCalc project
# @details This file contains the Equation class, which is used to store the equation its result and create the equation in the GUI
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk

from configuration import Config, ConfigDict
from equation_eval import eval_equation, create_assignment

from utils import rgb_to_tk

class Equation():
    """
    The equation class which stores the equation its result and contains
    the functions to display it in the GUI.
    """
    def __init__(self, equation: str, assignments: dict = dict(), theme_config: ConfigDict = None):
        """
        Create an equation class

        ### Params:
        equation : str
         The raw equation string
        theme_config
         The theme config to use
         
        assignments
         The dictionary of functions and variables available

        ### Variables:
        equation_str : str
         A string representation of the equation

        result : float or str
         The result of the equation

        frm_equation : str
         The outer frame of the equation

        type : str
         The type of equation: "None" (default), "expression", "comment",
         "variable", "function" this is set on __find_result()
        """
        self.assignments = assignments
        self.equation_str = equation
        self.type = "None"
        self.result = self.__find_result()


        self.theme = theme_config

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
        # Have to include globals otherwise current name space is used
        result = None
        
        if (self.equation_str[0] == "#"): # comment
            self.type = "comment"
        
        elif (self.equation_str[0].isalpha() and self.equation_str.find(":") != -1): 
            assignment = create_assignment(self.equation_str, self.assignments)
            
            self.assignments[assignment[0]] = assignment[1]

            self.type = "assignment"
            if (not callable(assignment[1])):
                result = assignment[1] # If variable report result
        
        else:
            result = eval_equation(self.equation_str, self.assignments)
            
            
            self.type = "equation"
                
        
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
        
        # Remove from assignments if necessary
        # if (self.type == "assignment"):
        #     self.assignments.pop()

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
        self.frm_equation.config(background=rgb_to_tk(self.theme.colours.background))
        
        # Create the equation components
        self.lbl_equation = tk.Label(self.frm_equation, text=self.equation_str, anchor="w")
        self.lbl_equation.grid(row=0, column=0, sticky="new")
        
        if (self.result != None):
            self.lbl_result = tk.Label(self.frm_equation, text="="+str(self.result), anchor="w")
            self.lbl_result.grid(row=1, column=0, sticky="new")
        else:
            self.lbl_result = tk.Label(self.frm_equation, text="", anchor="w")
            self.lbl_result.grid(row=1, column=0, sticky="new")
 
        self.btn_delete = tk.Button(self.frm_equation, command=self.delete_equation)
        
        self.btn_delete.grid(row=0, column=1, rowspan=2, padx=10)

        # Set theme
        self.lbl_equation.config(background=rgb_to_tk(self.theme.colours.background),
                                 font=(self.theme.font.family, self.theme.font.size))

        if (self.type == "comment"):
            self.lbl_equation.config(foreground=rgb_to_tk(self.theme.colours.comment))
        elif (self.type == "equation"):
            self.lbl_equation.config(foreground=rgb_to_tk(self.theme.colours.equation))
        elif (self.type == "assignment"):
            self.lbl_equation.config(foreground=rgb_to_tk(self.theme.colours.assignment))


        self.lbl_result.config(foreground=rgb_to_tk(self.theme.colours.result),
                               background=rgb_to_tk(self.theme.colours.background),
                               font=(self.theme.font.family, self.theme.font.size))            

        self.btn_delete.config(highlightthickness=0,
                                relief="flat",
                                background=rgb_to_tk(self.theme.colours.delete_button),
                                font=(self.theme.font.family, self.theme.font.size))

        # Set the delete function
        self.delete_function = delete_function


if __name__ == "__main__":
    equation1 = Equation("2+2")
    print(equation1)
    equation1.update_equation("2+3")
    print(equation1)

    equation1.create_equation(tk.Tk(), 0)
    tk.mainloop() # 2+3 \n =5
