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

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.title("Export History")

        self.minsize(300, 200)
        self.maxsize(300, 200)
        self.geometry("150x80")

        # Create entry points
        # File Name (text entry)
        # Title (text entry)
        # Comment (text window)
        # Format (drop down)
        # Create (button)
        self.ent_filename = tk.Entry(self, )
        self.ent_filename.focus_set()
        self.ent_filename.grid(row=0, column=0, sticky="nsew")

        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row=1, column=0, sticky="nsew")

        self.txt_comment = tk.Text(self, height=5, width=52)
        self.txt_comment.grid(row=2, column=0, sticky="nsew")

        formats = ["Markdown", "Latex", "Plain Text"]
        default_format = tk.StringVar(self)
        default_format.set(formats[0])

        self.drp_format = tk.OptionMenu(self, default_format, *formats)
        self.drp_format.grid(row=4, column=0, sticky="ns")

        self.btn_export = tk.Button(self, command=self.export_history)
        self.btn_export.grid(row = 5, column=0, sticky="nsew", padx=40)

    def export_history(self, event: tk.Event = None):
        """
        Export the history to the selected file format.

        ### Params:
        event : tk.Event
         The event object.
        """
