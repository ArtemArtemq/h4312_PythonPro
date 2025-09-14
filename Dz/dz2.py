from random import randint

class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.study_progress = 0
        self.money = 2000
        self.isStudent = True
    def to_study(self):
        print("Time to study")
        self.study_progress += 0.22
        self.happiness -= 4.2
        self.money -= 50 # на каву
    def to_sleep(self):
        print("Time to sleep")
        self.happiness += 1.8
    def to_chill(self):
        print("Chill time")
        money_spent = randint(50, 340)
        self.money -= money_spent
        self.happiness += 5.3
        self.study_progress -= 0.1
    def to_work(self):
        print("Work time")
        money_earned = randint(150, 200)
        self.money += money_earned
        self.happiness -= 2.9
        self.study_progress -= 0.02
    def is_alive(self):
        if self.study_progress < -0.5:
            print("!---Cast out---!")
            self.isStudent = False
        elif self.happiness <= 0:
            print("!---Depression---!")
            self.isStudent = False
        elif self.study_progress > 5:
            print("!---Passed externally---!")
            self.isStudent = False
        elif self.money <= -2000:
            print("!---Went bankrupt---!")
            self.isStudent = False
    def end_of_day(self):

        if self.study_progress >= 3.8: # стипедія
            print("Student receives a scholarship!")
            self.money += 30
        print(f"Happiness = {round(self.happiness, 2)}")
        print(f"Study progress = {round(self.study_progress, 2)}")
        print(f"Money = {round(self.money, 2)}")
    def live(self, day):
        text_day = f"Day {day} of {self.name} live"
        print(f"{text_day:=^30}")
        cube = randint(1, 4)
        if cube == 1:
            self.to_sleep()
        elif cube == 2:
            self.to_study()
        elif cube == 3:
            self.to_chill()
        else:
            self.to_work()
        self.end_of_day()
        self.is_alive()

artem = Student(name="Artem")

for day in range(0, 365):
    if artem.isStudent == False:
        break
    artem.live(day)
