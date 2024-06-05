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

class ScrollableFrame(tk.Frame):
    """
    The scrollable frame class that allows for easy scrollable frames.
    """
    def __init__(self, master: tk.Widget= None) -> None:
        """
        The constructor for the ScrollableFrame class

        ### Params:
        master : tk.Widget
         The master frame for the scrollable window

        ### Variables
        inner : tk.Frame
         The inner frame of the scrollable window used to place the internal objects
        """
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Create the canvas
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0, takefocus=0)

        # Create the scroll bar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind("<Configure>", self.__resize_inner)

        # Create the frame
        self.inner = tk.Frame(self.canvas, width=master.winfo_width(),)
        self.inner_id = self.canvas.create_window(0, 0, anchor='nw', window=self.inner)
        self.inner.bind("<Configure>", self.__update_scroll_region)

        # Layout
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

    def __resize_inner(self, event : tk.Event = None) -> None:
        """
        The callback function for the canvas interior resize operation.

        ### Params:
        event
         The event passed by tk
        """
        if self.inner.winfo_reqwidth() != self.inner.winfo_reqheight():
            # Update the inner frames width to fill the canvas
            self.canvas.itemconfigure(self.inner_id, width=self.canvas.winfo_width())

    def __update_scroll_region(self, event : tk.Event = None) -> None:
        """
        The callback function for the inner frame configure operation.

        ### Params:
        event : tk.Event
         The event passed by tk
        """
        # update scrollbar to match the size of the inner frame
        size = (event.width, event.height)
        self.canvas.config(scrollregion="0 0 %s %s" % size)
        
        if self.inner.winfo_reqwidth() != self.canvas.winfo_width():
            # update the canvas's width to fit the interior frame
            self.canvas.config(width=self.inner.winfo_reqwidth())

    def test_update(self):
        """
        Force an update to the scrollable frame
        """
        self.canvas.event_generate("<Configure>")
        self.inner.event_generate("<Configure>")

    def scroll(self, position: str):
        """
        Scroll the canvas to a given point

        ### Params:
        position: str
         The position to scroll to accepted: "bottom", "top", fraction of the height where 1 is the bottom
        """    
        if (position == "bottom"):
            self.canvas.yview_moveto(1)
        elif (position == "top"):
            self.canvas.yview_moveto(0)
        else:
            self.canvas.yview_moveto(float(position))

if __name__ == "__main__":
    root = tk.Tk()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create the scrollable frame
    scrollable_frame = ScrollableFrame(root)
    scrollable_frame.grid(row=0, column=0, sticky="nsew")

    # Create the widgets
    for i in range(50):
        ttk.Label(scrollable_frame.inner, text=f"Label {i}").grid(row=i, column=0)
    

    root.mainloop()

