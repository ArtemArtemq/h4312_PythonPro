try:
    print("start code")
    print(5/0)
    print("No errors")
except NameError:
    print("We have error NameError")
except ZeroDivisionError:
    print("We have error ZeroDivisionError")

print("code after capsule")