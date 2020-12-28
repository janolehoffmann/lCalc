#This file is part of lCalc which is released under the MIT License.
#See the file 'LICENSE' for full license details.

import math

def evaluate(input):
    input = __replace_functions(input)
    try:
        x = eval(input)
        return x
    except:
        return None


def __replace_functions(input):
    input = input.replace("sqrt", "math.sqrt")
    input = input.replace("pow", "math.pow")
    input = input.replace("^", "**")
    input = input.replace("log", "math.log")
    input = input.replace("factorial", "math.factorial")
    input = input.replace("sin", "math.sin")
    input = input.replace("cos", "math.cos")
    input = input.replace("tan", "math.tan")
    input = input.replace("pi", "math.pi")
    input = input.replace("e", "math.e")
    input = input.replace("\n", "")
    return input
