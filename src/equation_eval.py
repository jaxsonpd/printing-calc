## 
# @file equation_eval.py
# @author Jack Duignan (JackpDuignan@gmail.com)
# @date 2024-09-28
# @brief Provide functionality to allow for evaluation of complex equations

from typing import Union, Tuple
import math
import copy

FUNCTION_PLACEHOLDER_PARAMS = ["A192004", "B316294", "C449499", "D930100", "E733590"]

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
    equation_str = equation_str.replace("^^", "__XOR__")
    equation_str = equation_str.replace("^", "**")
    equation_str = equation_str.replace("__XOR__", "^")
    
    # try: 
    result = eval(equation_str, assignments) # Should never actually do this
    # except:
    #     result = "error"

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
    split_eq_str = equation_str.split(":=")
    name = split_eq_str[0].strip()
    name = name.split("(")[0] # remove function brackets

    assigne = split_eq_str[1]
    assignment = None

    if (equation_str.find("(") < equation_str.find(":") and equation_str.find("(") != -1): # Function
        parameters = split_eq_str[0][split_eq_str[0].find("(")+1:-1].split(",")
        parameters = [param.strip() for param in parameters]

        # Replace parameters with placeholder names
        for i in range(len(parameters)):
            assigne = assigne.replace(parameters[i], FUNCTION_PLACEHOLDER_PARAMS[i])

        def f(A192004=0, B316294=0, C449499=0, D930100=0, E733590=0, assigne=assigne, assignments=assignments):
            """
            The function to save. This uses random parameters (up to 5) to ensure no collisions
            """
            assignments = copy.deepcopy(assignments)
            
            # Add temp placeholders to allow function to execute
            assignments["A192004"] = A192004
            assignments["B316294"] = B316294
            assignments["C449499"] = C449499
            assignments["D930100"] = D930100
            assignments["E733590"] = E733590

            return eval_equation(assigne, assignments)
        
        assignment = f

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
