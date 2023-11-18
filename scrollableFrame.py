## @file scrollableFrame.py
# @brief A scrollable frame class
# @details This file contains the ScrollableFrame class, which allows for a frame to be scrolled
#          through if it is too big for the window
# @cite adapted from https://stackoverflow.com/questions/71677889/create-a-scrollbar-to-a-full-window-tkinter-in-python 
#       and https://blog.teclado.com/tkinter-scrollable-frames/
# @author Jack Duignan (JackpDuignan@gmail.com)

import tkinter as tk
from tkinter import ttk

## @class ScrollableFrame
# @brief The scrollable frame class
class ScrollableFrame(ttk.Frame):
    ## @brief The constructor for the ScrollableFrame class
    # @param self The object pointer
    # @param master The master widget to place the scrollable frame in
    def __init__(self, master: ttk.Widget= None) -> None:
        super().__init__(master)

        # Create the canvas
        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Create the scroll bar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create the frame
        self.frame = ttk.Frame(self.canvas)


if __name__ == "__main__":
    root = tk.Tk()
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    # Create the scrollable frame
    scrollable_frame = ScrollableFrame(root)
    scrollable_frame.grid(row=0, column=0, sticky="nsew")

    # Create the widgets
    for i in range(50):
        ttk.Label(scrollable_frame.frame, text=f"Label {i}").grid(row=i, column=0)

    # Configure the scrollable frame
    scrollable_frame.canvas.create_window((0, 0), window=scrollable_frame.frame, anchor="nw")
    scrollable_frame.frame.bind("<Configure>", lambda event: scrollable_frame.canvas.configure(scrollregion=scrollable_frame.canvas.bbox("all")))

    root.mainloop()

