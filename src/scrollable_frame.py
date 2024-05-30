## @file scrollableFrame.py
# @brief A scrollable frame class
# @details This file contains the ScrollableFrame class, which allows for a frame to be scrolled
#          through if it is too big for the window
# @cite adapted from https://stackoverflow.com/questions/71677889/create-a-scrollbar-to-a-full-window-tkinter-in-python 
#       and https://blog.teclado.com/tkinter-scrollable-frames/
# @cite good to look at https://stackoverflow.com/questions/3085696/adding-a-scrollbar-to-a-group-of-widgets-in-tkinter/3092341#3092341
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk

class ScrollableFrame():
    """
    The scrollable frame class that allows for easy scrollable frames.
    """
    def __init__(self, master: ttk.Widget= None) -> None:
        """
        The constructor for the ScrollableFrame class

        ### Params:
        master : ttk.Widget
         The master frame for the scrollable window

        ### Variables
        outer : tk.Frame
         The outer frame of the scrollable window used to place the window.

        inner : tk.Frame
         The inner frame of the scrollable window used to place the internal objects
        """
        self.outer = tk.Frame(master)
        self.outer.grid_columnconfigure(0, weight=1)
        self.outer.grid_rowconfigure(0, weight=1)

        # Create the canvas
        self.canvas = tk.Canvas(self.outer, borderwidth=0, highlightthickness=0, takefocus=0, background="red")

        # Create the scroll bar
        self.scrollbar = ttk.Scrollbar(self.outer, orient="vertical", command=self.canvas.yview)

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self._resize_interior)

        # Create the frame
        self.interior = tk.Frame(self.canvas, bg="red", width=master.winfo_width(),)
        self.interior_id = self.canvas.create_window(0, 0, anchor='nw', window=self.interior)
        self.interior.bind("<Configure>", self._update_scroll_region)

        # Layout
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

    def _resize_interior(self, event) -> None:
        """
        The callback function for the interior resize operation.

        ### Params:
        event
         The event passed by tk
        """
        if self.interior.winfo_reqwidth() != self.interior.winfo_reqheight():
            # Update the inner frames width to fill the canvas
            self.canvas.itemconfigure(self.interior_id, width=self.canvas.winfo_width())

    def _update_scroll_region(self, event) -> None:
        """
        The callback function for the interior scroll operation. (Not working Correctly)

        ### Params:
        event
         The event passed by tk
        """
        # update scrollbar to match the size of the inner frame
        size = (self.interior.winfo_reqwidth(), self.interior.winfo_reqheight())
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        
        if self.interior.winfo_reqwidth() != self.canvas.winfo_width():
            # update the canvas's width to fit the interior frame
            self.canvas.config(width=self.interior.winfo_reqwidth())

        self.canvas.yview_moveto(1)

if __name__ == "__main__":
    root = tk.Tk()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create the scrollable frame
    scrollable_frame = ScrollableFrame(root)
    scrollable_frame.outer.grid(row=0, column=0, sticky="nsew")

    # Create the widgets
    for i in range(50):
        ttk.Label(scrollable_frame.interior, text=f"Label {i}").grid(row=i, column=0)

    root.mainloop()

