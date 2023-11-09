## 
# @file equation.py
# @brief the Equation class for the printingCalc project
# @details This file contains the Equation class, which is used to store the equation its result and create the equation in the GUI
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk

## @class Equation
# @brief Stores the equation and its result and contains modules to create the equation in the GUI
class Equation():
    ## @brief The constructor for the Equation class
    # @param self The object pointer
    # @param equation The equation string to store
    def __init__(self, equation: str):
        self.equation_str = equation
        self.result = self.__find_result()
    
        ## @brief Find the result of the equation
    # @param self The object pointer
    # @return The result of the equation None if the equation is invalid
    def __find_result(self):
        try:
            result = eval(self.equation_str)
        except:
            result = None
        
        return result
    
    ## @brief Update the equation in the class
    # @param self The object pointer
    # @param equation The new equation string
    def update_equation(self, equation: str):
        self.equation_str = equation
        self.result = self.__find_result()
    
    ## @brief Creates the equation in the GUI
    # @param self The object pointer
    # @param master The master widget to place the equation in
    # @param row The row to place the equation in
    # @param column The column to place the equation in default=0
    # @param sticky The sticky value for the equation default="sew" (bottom)
    def create_equation(self, master: tk.Widget, row: int, column: int = 0, sticky: str = "sew"):
        # Create the equation frame
        self.frm_equation = tk.Frame(master)
        self.frm_equation.columnconfigure(0, weight=1)
        self.frm_equation.grid(row=row, column=column, sticky=sticky)

        self.lbl_equation = tk.Label(self.frm_equation, text=self.equation_str, height=1, width=10, anchor="w")
        self.lbl_equation.grid(row=0, column=0, sticky="new")
        self.lbl_answer = tk.Label(self.frm_equation, text="="+str(self.result), height=1, width=10, anchor="w")
        self.lbl_answer.grid(row=1, column=0, sticky="new")
        
        self.btn_delete = tk.Button(self.frm_equation, text="x", height=1, width=1, command=lambda: self.frm_equation.destroy())
        self.btn_delete.grid(row=0, column=1, rowspan=2, padx=10)

    


if __name__ == "__main__":
    equation1 = Equation("2+2")
    print(equation1.result) # 4
    equation1.update_equation("2+3")
    print(equation1.result) # 5

    equation1.create_equation(tk.Tk(), 0)
    tk.mainloop() # 2+3 \n =5
