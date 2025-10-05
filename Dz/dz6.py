result = []
def divider(a, b):
    try:
        if a == "123" or a < b:
            print("Value error")
            raise ValueError
        if b > 100:
            print("Index error")
            raise IndexError
        print("divider is complete \n")
        return a/b
    except:
        print("divider is not complete \n")

try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
except:
    print("TypeError")
    data = {10: 2, 2: 5, "123": 4, 18: 0, 9: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
    except:
        print("Name error")
        res = divider(key, data[key])
    result.append(res)

print(result)