## @file history.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The history portion implemented as a scrollable frame

import tkinter as tk
from tkinter import ttk

from scrollable_frame import ScrollableFrame


class History():
    """
    This class displays the equations in a scrollable format.
    """
    def __init__(self, master: ttk.Widget = None, row: int = 0):
        """
        The constructor for the History class

        ### Params:
        master : ttk.Widget
         The master frame for the history window to be placed inside of.
        
        row : int
         The row of the frame for the history window to appear in.
        """
        # Setup the scrollable frame
        self.scrollableFrame = ScrollableFrame(master) 
        self.scrollableFrame.outer.grid(row=row, column=0, sticky="nsew")

        # Allow the frame to resize
        self.scrollableFrame.interior.rowconfigure(0, weight=1)
        self.scrollableFrame.interior.columnconfigure(0, weight=1)