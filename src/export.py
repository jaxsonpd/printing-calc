## @file export.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-06-07
#  @brief The implementation of the export window that allows for 
#  exporting the current history

from configuration import Config

from history import History
import tkinter as tk

class ExportWindow(tk.Toplevel):
    """
    The export window main class which creates the window etc.
    """
    def __init__(self, history: History) -> None:
        """
        Create an export window

        ### Params:
        history : History
         The history to use in the export
        """
        super().__init__()

        self.title("Export History")

        self.minsize(300, 200)
        self.geometry("150x80")

