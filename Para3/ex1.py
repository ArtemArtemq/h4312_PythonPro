class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def print_passenger(self):
        if self.passengers != []:
            print(f"Names: {self.brand} passenger")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"{self.brand} are not passenger")

person1 = Human("Vova")
person2 = Human("Artem")
person3 = Human("Dima")

car = Auto("Mersedes")
car.add_passenger(person1)
car.add_passenger(person2)
car.add_passenger(person3)
car.print_passenger()
