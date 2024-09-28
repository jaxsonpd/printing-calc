## 
# @file equation_eval.py
# @author Jack Duignan (JackpDuignan@gmail.com)
# @date 2024-09-28
# @brief Provide functionality to allow for evaluation of complex equations

from typing import Union, Tuple
import math

def eval_equation(equation_str: str, assignments: dict) -> float:
    """
    Evaluate the given equation

    ### Params:
    equation_str
     The equation string
    assignments
     The dictionary of functions and variables available
    
    ### Returns:
    result
     The result of the equation
    """
    try: 
        result = eval(equation_str, assignments)
    except:
        result = "error"

    return result

def create_assignment(equation_str: str, assignments: dict) -> Tuple[str, Union[callable, float]]:
    """
    Create a variable 
    ### Params:
    equation_str
     The equation string

    assignments
     The dictionary of functions and variables available
    
    ### Returns:
    (name, assignment)
     The name of the assignment and the assignment ether variable or callable
    """
    split_eq_str = equation_str.split(":")
    name = split_eq_str[0].strip()
    assigne = split_eq_str[1][1:]

    assignment = None

    if (equation_str.find("(") < equation_str.find(":") and equation_str.find("(") != -1): # Function
        pass
    else: # variable
        assignment = eval_equation(assigne, assignments)

    return (name, assignment)


def default_assignments(assignments: dict):
    """
    Populate the assignments dictionary with the default assignments

    ### Params:
    assignments
     The empty assignments dictionary
    """
    assignments["pi"] = 3.14159265359
    assignments["sin"] = math.sin
    assignments["cos"] = math.cos
    assignments["tan"] = math.tan

    assignments["exp"] = math.exp
