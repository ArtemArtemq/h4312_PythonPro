def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"Sorry, we can`t work with {type(var_1)}")
    else:
        return var_1

a = 1
checker(a)