from random import randint

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.13
        self.gladness -= 4.2
    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 1.8
    def to_chill(self):
        print("Rest time")
        self.gladness += 3.5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        text_day = f"Day {day} of {self.name} live"
        print(f"{text_day:=^30}")
        cube = randint(1, 3)
        if cube == 1:
            self.to_sleep()
        elif cube == 2:
            self.to_study()
        else:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

artem = Student(name="Artem")

for day in range(0, 365):
    if artem.alive == False:
        break
    artem.live(day)