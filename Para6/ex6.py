class NumberErrorForArtem(Exception):
    def __str__(self):
        return f"You wrote the numbers in the wrong order"

class DivisionErrorForArtem(Exception):
    def __str__(self):
        return f"You wanted to divide by zero, but you can't do that"

first_number = int(input("Write first number: "))
second_number = int(input("Write second number: "))

if second_number == 0:
    raise DivisionErrorForArtem
elif first_number >= second_number:
    print(first_number/second_number)
else:
    raise NumberErrorForArtem