import math

def evaluate(input):
    try:
        input = input.replace("sqrt", "math.sqrt")
        input = input.replace("pow", "math.pow")
        input = input.replace("log", "math.log")
        input = input.replace("factorial", "math.factorial")

        input = input.replace("sin", "math.sin")
        input = input.replace("cos", "math.cos")
        input = input.replace("tan", "math.tan")

        input = input.replace("pi", "math.pi")
        input = input.replace("e", "math.e")

        x = eval(input)
        return x
    except:
        return None
