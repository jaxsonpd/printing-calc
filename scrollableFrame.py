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

        # Create the scroll bar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        # Configure the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create the frame
        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window(0, 0, anchor='nw', window=self.frame)
        self.frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.canvas.pack(fill='both', expand=True, side='left')
        self.scrollbar.pack(fill='y', side='right')
        self.frame.pack(fill='both', expand=True)

    def return_frame(self):
        return self.frame

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

    root.mainloop()

