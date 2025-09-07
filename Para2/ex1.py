class Student:
    def __init__(self, height = 170):
        self.height = height


artem = Student()
vova = Student(height=180)

print(artem.height)
print(vova.height)