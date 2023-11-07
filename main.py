## 
# @file main.py
# @brief Main file for the printingCalc project
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Set up the window
        self.master.title("Printing Calculator")

        self.master.maxsize(750, 500)
        self.master.minsize(500, 250)

        # Create the menu bar
        menuBar = tk.Menu(self.master)

        # File menu
        filemenu = tk.Menu(menuBar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.master.quit)

        # Add menus to the menu bar
        menuBar.add_cascade(label="File", menu=filemenu)
        self.master.configure(menu=menuBar)

        # Set up the master grid
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)


        # Create the history frame
        self.frm_history = tk.Frame(self.master)
        self.frm_history.columnconfigure(0, weight=1)
        self.frm_history.grid(row=0, column=0, sticky="nsew")

        # Create the history widgets
        self.frm_result = tk.Frame(self.frm_history, background="blue") # A frame to hold a result
        self.frm_result.columnconfigure(0, weight=1)
        self.frm_result.grid(row=0, column=0, sticky="new")

        self.lbl_result_equation = tk.Label(self.frm_result, text="2+2", height=1, width=10, anchor="w")
        self.lbl_result_equation.grid(row=0, column=0, sticky="new")
        self.lbl_result_answer = tk.Label(self.frm_result, text="4", height=1, width=10, anchor="w")
        self.lbl_result_answer.grid(row=1, column=0, sticky="new")
        
        self.btn_result_delete = tk.Button(self.frm_result, text="x", height=1, width=1)
        self.btn_result_delete.grid(row=0, column=1, rowspan=2, padx=10)


        self.frm_result2 = tk.Frame(self.frm_history, background="red") # A frame to hold a result
        self.frm_result2.columnconfigure(0, weight=1)
        self.frm_result2.grid(row=1, column=0, sticky="new")

        self.lbl_result_equation2 = tk.Label(self.frm_result2, text="2+3", height=1, width=10, anchor="w")
        self.lbl_result_equation2.grid(row=0, column=0, sticky="new")
        self.lbl_result_answer2 = tk.Label(self.frm_result2, text="5", height=1, width=10, anchor="w")
        self.lbl_result_answer2.grid(row=1, column=0, sticky="new")
        
        self.btn_result_delete2 = tk.Button(self.frm_result2, text="x", height=1, width=1)
        self.btn_result_delete2.grid(row=0, column=1, rowspan=2, padx=10)


        self.frm_result3 = tk.Frame(self.frm_history, background="yellow") # A frame to hold a result
        self.frm_result3.columnconfigure(0, weight=1)
        self.frm_result3.grid(row=2, column=0, sticky="new")

        self.lbl_result_equation3 = tk.Label(self.frm_result3, text="2+4", height=1, width=10, anchor="w")
        self.lbl_result_equation3.grid(row=0, column=0, sticky="new")
        self.lbl_result_answer3 = tk.Label(self.frm_result3, text="6", height=1, width=10, anchor="w")
        self.lbl_result_answer3.grid(row=1, column=0, sticky="new")
        
        self.btn_result_delete3 = tk.Button(self.frm_result3, text="x", height=1, width=1)
        self.btn_result_delete3.grid(row=0, column=1, rowspan=2, padx=10)

        # Create the equation frame
        self.frm_equation = tk.Frame(self.master)
        self.frm_equation.rowconfigure(0, weight=1)
        self.frm_equation.columnconfigure(0, weight=1)

        self.frm_equation.grid(row=1, column=0, sticky="nsew")

        # Create the equation widgets
        self.ent_equation = tk.Entry(self.frm_equation)
        self.ent_equation.grid(row=0, column=0, sticky="nsew")



myapp = App()

# start the program
myapp.mainloop()