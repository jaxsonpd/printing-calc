## @file utils.py
#  @author Jack Duignan (JackpDuignan@gmail.com)
#  @date 2024-06-05
#  @brief This file provides helpful utilities for use in the rest of the app.

def rgb_to_tk(rgb: tuple) -> str:
    """
    Converts from rgb to a hex str for use in tkinter colour settings.

    ### Params:
    rgb : tuple
     The rgb values in (r, g, b) form
    """
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"