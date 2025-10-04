def calculate(expression):
    try:
        try:
            if (eval(expression) == float(expression)):
                raise NameError
        except ValueError:
            return eval(expression)
    except ZeroDivisionError:
        print("На нуль ділити не можна!")
        return
    except (NameError, SyntaxError):
        print("Ви мали ввести математичний вираз!")
        return

while (True):
    expression = input("Введіть математичний вираз: ")
    result = calculate(expression)
    if (result != None):
        print(result)