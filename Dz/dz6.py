class ValueError(Exception):
    def __str__(self):
        return f"Value Error"

class IndexError(Exception):
    def __str__(self):
        return f"Index Error"

class TypeErrorForArtem(Exception):
    def __str__(self):
        return f"Type Error"

result = []
def divider(a, b):
    if a < b:
        raise ValueError

    if b > 100:
        raise IndexError

    if a == [] or a == "123":
        raise TypeErrorForArtem

    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 9: 15, 8 : 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)