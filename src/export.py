## @file export.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-06-07
#  @brief The implementation of the export window that allows for 
#  exporting the current history

import tkinter as tk
import tkinter.messagebox as tk_msg
import datetime

from configuration import Config, ConfigDict
from utils import rgb_to_tk
from history import History

def export_txt(history: History, filename: str, title: str, comment: str):
    """
    Export the current history as a txt file

    ### Params:
    history
        The history to save
    filename
        The filename to save to (without type)
    title
        The title to write at the beginning of the file
    comment
        The comment to add after the title
    """
    full_filename = filename + ".txt"

    with open(full_filename, "w") as f:
        if (len(title) != 0):
            f.write("Title: " + title + "\n\n")
        if (len(comment) != 0):
            f.write("Comment:\n" + comment + "\n\n")

        for equation in history.equations:
            if (equation.type == "comment"):
                f.write(equation.equation_str[1:].strip() + "\n")
            elif (equation.type == "equation"):
                f.write(equation.equation_str + "\n")
                f.write("= " + str(equation.result) + "\n")

        f.write("\n-- Printing Calc History --" + "\n" + "Export Time: " + str(datetime.datetime.now())[:-7])

def export_md(history: History, filename: str, title: str, comment: str):
    """
    Export the current history as a markdown file

    ### Params:
    history
        The history to save
    filename
        The filename to save to (without type)
    title
        The title to write at the beginning of the file
    comment
        The comment to add after the title
    """
    full_filename = filename + ".md"

    with open(full_filename, "w") as f:
        if (len(title) != 0):
            f.write("# " + title + "\n\n")
        if (len(comment) != 0):
            f.write(comment.replace("\n", "\n\n") + "\n\n")

        f.write("### Content: \n\n")

        for equation in history.equations:
            if (equation.type == "comment"):
                f.write(equation.equation_str[1:].strip() + "\n\n")
            elif (equation.type == "equation"):
                f.write("$$\n")
                f.write(equation.equation_str + "\n")
                f.write("= " + str(equation.result) + "\n")
                f.write("$$\n\n")

        f.write("---\n")
        f.write("\n ### Printing Calc History" + "\n\n" + "**Export Time:** " + str(datetime.datetime.now())[:-7])

class ExportWindow(tk.Toplevel):
    """
    The export window main class which creates the window etc.
    """
    def __init__(self, history: History, theme_config: ConfigDict = None) -> None:
        """
        Create an export window

        ### Params:
        history : History
         The history to use in the export
        """
        super().__init__()

        self.history = history

        self.theme = theme_config

        self.create_window()
        

    def create_window(self):
        """
        Create the export window
        """
        self.rowconfigure(3, weight=1)
        # self.columnconfigure(0, weight=0.5)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.title("Export History")
        self.config(background=rgb_to_tk(self.theme.colours.background))

        self.minsize(300, 300)
        self.maxsize(800, 600)
        self.geometry("300x300")

        self.lbl_filename = tk.Label(self, text="Filename:", anchor="w", padx=0)
        self.lbl_filename.grid(row=0, column=0, sticky="nsew")
        self.ent_filename = tk.Entry(self)
        self.ent_filename.insert(0, "pc-export")
        self.ent_filename.focus_set()
        self.ent_filename.grid(row=0, column=1, sticky="nsew", columnspan=2)

        self.lbl_title = tk.Label(self, text="Title:", anchor="w")
        self.lbl_title.grid(row=1, column=0, sticky="nsew")
        self.ent_title = tk.Entry(self)
        self.ent_title.insert(0, "pc-export")
        self.ent_title.grid(row=1, column=1, sticky="nsew", columnspan=2)

        self.lbl_comment = tk.Label(self, text="Comment:")
        self.lbl_comment.grid(row=2, column=0, sticky="nsew", columnspan=3)
        self.txt_comment = tk.Text(self, height=5, width=52)
        self.txt_comment.grid(row=3, column=0, sticky="nsew", columnspan=3)

        formats = ["Markdown", "Latex (Not Implemented)", "Plain Text"]
        self.str_sel_format = tk.StringVar(self)
        self.str_sel_format.set(formats[2])

        self.drp_format = tk.OptionMenu(self, self.str_sel_format, *formats)
        self.drp_format.grid(row=4, column=0, sticky="ns")

        self.btn_export = tk.Button(self, command=self.export_history, text="Export")
        self.btn_export.grid(row = 4, column=1, sticky="ns", padx=40, columnspan=2)

        # Apply Theme
        for entry in [self.ent_filename, self.ent_title, self.txt_comment]:
            entry.config(background=rgb_to_tk(self.theme.colours.entry_background),
                        foreground=rgb_to_tk(self.theme.colours.entry_text),
                        relief="flat",
                        insertbackground="white",
                        highlightcolor="white",
                        highlightthickness=0,
                        insertwidth=1,
                        font=(self.theme.font.family, self.theme.font.size))
        
        for label in [self.lbl_filename, self.lbl_title, self.lbl_comment]:
            label.config(background=rgb_to_tk(self.theme.colours.background),
                        foreground=rgb_to_tk(self.theme.colours.comment),
                        font=(self.theme.font.family, self.theme.font.size))

        for button in [self.btn_export, self.drp_format]:
            button.config(background=rgb_to_tk(self.theme.colours.other_button_background),
                        foreground=rgb_to_tk(self.theme.colours.other_button_text),
                        font=(self.theme.font.family, self.theme.font.size))

    def export_history(self, event: tk.Event = None):
        """
        Export the history to the selected file format.

        ### Params:
        event : tk.Event
         The event object.
        """
        # Get and Check file name
        filename: str = self.ent_filename.get()
        
        if (filename.find(" ") != -1 or len(filename) == 0): # space is present
            self.ent_filename.config(foreground="red")
            tk_msg.showwarning(title="Bad Filename", parent=self,message="Bad Filename:\n" +
                                "Filename must not include spaces and must not be empty.") 
            
            return

        # Get title
        title: str = self.ent_title.get()

        # Get comment
        comment: str = self.txt_comment.get(1.0, "end-1c")

        # Export
        if (self.str_sel_format.get() == "Plain Text"):
            export_txt(self.history, filename, title, comment)
        elif (self.str_sel_format.get() == "Markdown"):
            export_md(self.history, filename, title, comment)
    
    

    
