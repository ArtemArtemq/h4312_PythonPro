from random import randint
import  logging

logging.basicConfig(level=logging.DEBUG,
                    filename="Sims_logs",
                    filemode="w")

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        logging.debug("Time to study")
        self.progress += 0.11
        self.gladness -= 3
    def to_study_in_itStep(self):
        logging.debug("Time to study in itStep")
        self.progress += 0.21
        self.gladness -= 6.1
    def to_sleep(self):
        logging.debug("Time to sleep")
        self.gladness += 2.1
    def to_chill(self):
        logging.debug("Rest time")
        self.gladness += 4.5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            logging.debug("Cast out")
            self.alive = False
        elif self.gladness <= 0:
            logging.debug("Depression")
            self.alive = False
        elif self.progress > 5:
            logging.debug("Passed externally")
            self.alive = False
    def end_of_day(self):
        logging.debug(f"Gladness = {self.gladness}")
        logging.debug(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        text_day = f"Day {day} of {self.name} live"
        logging.debug(f"{text_day:=^30}")
        cube = randint(1, 4)
        if cube == 1:
            self.to_sleep()
        elif cube == 2:
            self.to_study()
        elif cube == 3:
            self.to_chill()
        else:
            self.to_study_in_itStep()
        self.end_of_day()
        self.is_alive()

artem = Student(name="Artem")

for day in range(0, 365):
    if artem.alive == False:
        break
    artem.live(day)