import inspect
import colorama

help(colorama)

ca = colorama

print(colorama.__name__)
print(ca.__name__, "\n")


print(inspect.ismodule(ca))
print(inspect.isclass(ca))
print(inspect.isfunction(ca))