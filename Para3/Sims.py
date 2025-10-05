import random

brands_of_car = {
    "BMW":{"fuel": 100, "strength": 100, "consumption": 6},
    "Lada":{"fuel": 50, "strength": 40,"consumption": 10},
    "Volvo":{"fuel": 70, "strength": 150,"consumption": 8},
    "Ferrari":{"fuel": 80, "strength": 120,"consumption": 14}
}

job_list = {
    "Java developer":{"salary": 50, "gladness_less": 10},
    "Python developer":{"salary": 40, "gladness_less": 10},
    "C++ developer":{"salary": 45, "gladness_less": 25},
    "C# developer":{"salary": 30, "gladness_less": 5}
}

pet_list = {
    "Parrot":{"maintenance":5, "gladness_great":2},
    "Cat European Shorthair": {"maintenance": 9, "gladness_great": 4},
    "Cat British Shorthair": {"maintenance": 13, "gladness_great": 6},
    "Dog Yorkshire Terrier": {"maintenance": 7, "gladness_great": 4}
}

class Human:
    def __init__(self, name="Human", job=None, car=None, house=None, pet=None):
        self.name = name
        self.job = job
        self.car = car
        self.house = house
        self.pet = pet
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_house(self):
        self.house = House()
        print("Settled in the house")
    def get_car(self):
        self.car = Auto(brands_of_car)
        print(f"I bought a car {self.car.brand}")
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
        print(f"I don't have a job, I'm going to get a job {self.job.job} with salary {self.job.salary}")
    def get_pet(self):
        self.pet = Pet(pet_list)
        print(f"I bought a pet {self.pet.species}")
    def to_eat(self):
        if self.house.food <= 0:
            self.to_shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
            return
        self.satiety += 5
        self.house.food -= 5
    def to_work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.to_shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

        self.pet.grieve()
    def to_shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            self.money -= 50
            self.house.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

        self.pet.grieve()
    def to_chill(self):
        self.gladness += 10
        self.house.mess += 5
    def to_play_with_pet(self):
        self.gladness += self.pet.gladness_great
        self.pet.play()
    def to_pet_feed(self):
        self.money -= self.pet.maintenance
        self.house.mess += 3
        self.pet.eat()
    def to_clean_house(self):
        self.gladness += 5
        self.house.mess = 0

        self.pet.grieve()
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

        self.pet.grieve()
    def day_index(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")

        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        print(f"Money – {self.money}")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}")

        house_indexes = "Home indexes"
        print(f"{house_indexes:^50}", "\n")
        print(f"Food – {self.house.food}")
        print(f"Mess – {self.house.mess}")

        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"Fuel – {self.car.fuel}")
        print(f"Strength – {self.car.strength}")

        pet_indexes = f"{self.pet.species} pet indexes"
        print(f"{pet_indexes:^50}", "\n")
        print(f"{self.pet.species}`s gladness - {self.pet.gladness}")
        print(f"{self.pet.species}`s satiety - {self.pet.satiety}")
    def is_alive(self):
        if self.gladness <= 0:
            print("Depression....")
            return False
        elif self.satiety <= 0:
            print("Dead")
            return False
        elif self.money < -500:
            print("Bankrupt")
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.house is None:
            self.get_house()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        if self.pet is None:
            self.get_pet()

        if self.satiety < 20:
            print("I'll go eat")
            self.to_eat()
        elif self.gladness < 20:
            if self.house.mess > 15:
                print("I want to chill, but there is so much mess…\nSo I will clean the house")
                self.to_clean_house()
            else:
                print("Let`s chill!")
                self.to_chill()

        elif self.money < 0:
            print("Start working")
            self.to_work()

        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()

        elif self.pet.gladness < 20:
            print("I will play with my pet")
            self.to_play_with_pet()

        elif self.pet.satiety < 20:
            print("I feed my pet")
            self.to_pet_feed()

        self.random_pick_active()

        self.day_index(day)

    def random_pick_active(self):
        dice = random.randint(1, 5)

        if dice == 1:
            print("Let`s chill!")
            self.to_chill()
        elif dice == 2:
            print("Start working")
            self.to_work()
        elif dice == 3 and self.house.mess > 0:
            print("Cleaning time!")
            self.to_clean_house()
        elif dice == 4:
            print("Time for treats!")
            self.to_shopping(manage="delicacies")
        elif dice == 5:
            print("I will play with my pet")
        else:
            self.random_pick_active()

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            print("The car cannot move!")
            return False

class Pet:
    def __init__(self, pet_list):
        self.species = random.choice(list(pet_list))
        self.maintenance = pet_list[self.species]["maintenance"]
        self.gladness_great = pet_list[self.species]["gladness_great"]
        self.gladness = 50
        self.satiety = 50
    def play(self):
        self.gladness += 12
        self.satiety -= 8
    def eat(self):
        self.gladness += 4
        self.satiety += 16
    def grieve(self):
        self.gladness -= 8
        self.satiety -= 6

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

Artem = Human("Artem")

for day in range(1, 31):
    if Artem.live(day) == False:
        break