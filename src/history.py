
## @file history.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The history portion implemented as a scrollabe frame

import tkinter as tk
from tkinter import ttk

from scrollable_frame import ScrollableFrame

## @class History
# @brief The history class
class History():
    ## @brief The constructor for the History class
    # @param self The object pointer
    # @param master The master widget to place the history in
    def __init__(self, master: ttk.Widget = None, row: int = 0):
        self.scrollableFrame = ScrollableFrame(master) 
        self.scrollableFrame.outer.grid(row=row, column=0, sticky="nsew")

        self.scrollableFrame.interior.rowconfigure(0, weight=1)
        self.scrollableFrame.interior.columnconfigure(0, weight=1)
        self.scrollableFrame.interior.grid(row=0, column=0, sticky="nsew")