## @file history.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-05-28
#  @brief The history portion implemented as a scrollable frame

import tkinter as tk
from tkinter import ttk

from scrollable_frame import ScrollableFrame


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
         
        """
        # Setup the scrollable frame
        super().__init__(master)

        # Allow the frame to resize
        self.inner.rowconfigure(0, weight=1)
        self.inner.columnconfigure(0, weight=1)