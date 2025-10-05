try:
    try:
        print("start code")
        #print(dfdsefdsfesdf)
        print("No errors")
    except SyntaxError:
        print("We have error SyntaxError")
except NameError as error:
    print(error)
else:
    print("No problem")
print("code after capsule")