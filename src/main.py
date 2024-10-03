## 
#  @file main.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The main file for the printing calculator project

import tkinter as tk
from tkinter import ttk
import os
import sys

from configuration import ConfigDict, Config
from equation import Equation
from menu_bar import MenuBar
from equation_entry import EquationEntry
from history import History

def get_cwd() -> str:
    """
    Get the current working directory of the application

    ### Returns
    directory
        The full current working directory path
    """
    getcwd = os.getcwd()
    argv_0 = sys.argv[0]

    # Remove file name from argv
    i = len(argv_0)-1
    while (argv_0[i] != "\\" and i != 0):
        i -= 1

    argv_0 = argv_0[:i] 

    if (argv_0[0:2] == "C:"): # Running in a stand alone application
        return argv_0
    else:
        return os.getcwd() + "\\" + argv_0
    
def load_theme(theme_path: str) -> ConfigDict:
    """
    Load the colour theme
    
    ### Params:
    theme_path
     Path to the theme json file

    ### Returns:
    theme_config
     The theme config dict
    """
    theme_config = Config.load_json(theme_path)

    return theme_config


class App(tk.Tk):
    """
    The main application class
    """
    def __init__(self):
        """
        Initialise a new GUI application 
        """
        super().__init__()

        # Set up the master grid
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.__setup_window()

        self.theme_config = load_theme(get_cwd()+"/theme.json")

        # Create the history
        self.history = History(self, theme_config=self.theme_config)
        self.history.grid(row=0, column=0, sticky="nsew")

        # Create the menu bar
        self.menu_bar = MenuBar(self, [self.history], theme_config=self.theme_config)

        # Create the equation entry
        self.equation_entry = EquationEntry(self, add_equation_function=self.add_equation, theme_config=self.theme_config)
        self.equation_entry.grid(row=1, column=0, sticky="nsew")

    def add_equation(self, equation_str):
        """
        Add a new equation to the history. Called by the equation entry.

        ### Params:
        equation_str
         The equation to add
        """
        equation = Equation(equation_str, self.history.assignments, theme_config=self.theme_config)

        # Add created equation to the gui
        equation.create_equation(self.history.inner, delete_function=self.history.remove_equation)
        equation.frm_equation.grid(row=len(self.history.equations), column=0, sticky="ew")

        self.history.equations.append(equation)

        self.update_idletasks()

        self.history.scroll("bottom")

        return True

    def __setup_window(self):
        """
        Create the main application window
        """
        # Set up the window
        self.title("Printing Calculator")

        self.minsize(500, 250)
        self.geometry("500x250")

    def start (self):
        """
        Start the printing calculator app
        """
        self.mainloop()


myapp = App()

# start the program
myapp.start()