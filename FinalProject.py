import random

class Wolf:
    def __init__(self, health=100, mood=0, satiety=50, strength=10, index_in_flock=0):
        self.health = health
        self.mood = mood
        self.satiety = satiety
        self.strength = strength
        self.index_in_flock = index_in_flock
    def add_health(self, value):
        if self.health + value < 100:
            self.health += value
        else:
            self.health = 100
    def add_mood(self, value):
        if self.mood + value < 15:
            self.mood += value
        else:
            self.mood = 15
    def add_satiety(self, value):
        if self.satiety + value < 100:
            self.satiety += value
        else:
            self.satiety = 100
    def add_strength(self, value):
        if self.strength + value < 20:
            self.strength += value
        else:
            self.strength = 20
    def hunt(self):
        self.satiety -= 6.2
        if random.randint(1, 100) < 50 + self.strength + self.mood:
            prey_weight = random.randint(19, 25)
            self.add_mood(prey_weight / 20)
            self.add_strength(0.4)
            return prey_weight
        else:
            self.mood -= 1
            return 0
    def relax(self):
        self.add_mood(1.3)
        if self.satiety >= 60 and self.mood >= 7:
            self.add_health(6)
    def end_day(self):
        self.satiety -= 4.6
        if self.satiety >= 85 and self.mood >= 9:
            self.add_health(12)
        if self.satiety <= 0:
            self.health -= 18
        if self.health <= 0 or self.mood <= -15:
            return False
        return True
class Flock:
    def __init__(self):
        self.number_enemy_flocks = random.randint(3, 4)
        self.wolfs = []
        self.average_health = 0
        self.average_mood = 0
        self.average_satiety = 0
        self.average_strength = 0

        for i in range(random.randint(4, 5)):
            wolf_health = random.randint(80, 100)
            wolf_mood = random.randint(-2, 2)
            wolf_satiety = random.randint(45, 70)
            wolf_strength = random.randint(8, 14)
            new_wolf = Wolf(health=wolf_health,
                            mood=wolf_mood,
                            satiety=wolf_satiety,
                            strength=wolf_strength)
            self.add_wolf(new_wolf)
    def add_wolf(self, wolf):
        print(f"До нас приєднався новий вовк з силою {wolf.strength}")
        wolf.index_in_flock = len(self.wolfs)
        self.wolfs.append(wolf)
    def remove_wolf(self, wolf):
        print(f"Нажаль, нас покидає вовк з силою {wolf.strength}")
        self.wolfs.pop(wolf.index_in_flock)
        index = 0
        for wolf in self.wolfs:
            wolf.index_in_flock = index
            index += 1
    def calculate_values(self):
        max_health = 0
        max_mood = 0
        max_satiety = 0
        max_strength = 0
        for wolf in self.wolfs:
            max_health += wolf.health
            max_mood += wolf.mood
            max_satiety += wolf.satiety
            max_strength += wolf.strength
        self.average_health = max_health / len(self.wolfs)
        self.average_mood = max_mood / len(self.wolfs)
        self.average_satiety = max_satiety / len(self.wolfs)
        self.average_strength = max_strength / len(self.wolfs)
    def to_hunting(self):
        prey_weight = 0
        successful_hunt = 0
        for wolf in self.wolfs:
            wolf_prey_weight = wolf.hunt()
            if wolf_prey_weight > 0:
                successful_hunt += 1
                prey_weight += wolf_prey_weight

        prey_weight_for_everyone = prey_weight / len(self.wolfs)
        print(f"Ми пішли на полювання. Всього {successful_hunt} вовків щось вполювало")
        print(f"Загальна вага здобичи склала {round(prey_weight, 2)} кг, це по {round(prey_weight_for_everyone, 2)} кг на кожного")
        for wolf in self.wolfs:
            wolf.add_satiety(prey_weight_for_everyone)
    def to_fake_fights(self):
        print("Вовки вирішили непосправжньому побитися між собою, щоб покращити свої навички")
        fight_number = 0
        wolf_index = 0
        for wolf_1 in self.wolfs:
            if wolf_index % 2 == 0 and wolf_index + 1 <= len(self.wolfs) - 1:
                fight_number += 1
                wolf_2 = self.wolfs[wolf_index + 1]
                if wolf_1.strength + wolf_1.mood > wolf_2.strength + wolf_2.mood:
                    print(f"За резутьтатами {fight_number} битви переміг перший вовк")
                    wolf_1.add_mood(2.8)
                elif wolf_1.strength + wolf_1.mood < wolf_2.strength + wolf_2.mood:
                    print(f"За резутьтатами {fight_number} битви переміг другий вовк")
                    wolf_2.add_mood(2.8)
                else:
                    print(f"За резутьтатами {fight_number} битви булі нічія")
                    wolf_1.add_mood(0.2)
                    wolf_2.add_mood(0.2)
                wolf_1.satiety -= 9.4
                wolf_2.satiety -= 9.4
                wolf_1.add_strength(1.2)
                wolf_2.add_strength(1.2)

            wolf_index += 1
    def to_relax(self):
        for wolf in self.wolfs:
            wolf.relax()
    def pick_active(self):
        massage = "Оберіть активність на день:"
        print(f"\n{massage:=^42}")
        print("1: Піти на полювання                     (настрій+- ситість+ сила+-)")
        print("2: Влаштувати несправжні бійки між собою (настрій+- ситість- сила+)")
        print("3: Відпочити в лігві                     (здоров'є+ настрій+)")
        print("4: Піти на бійку з іншею зграєю          (здоров'є- настрій+- ситість--)")
        is_choice_correct = False
        while (is_choice_correct == False):
            try:
                choice = int(input("Введіть номер, що будемо робити (1-4) "))
                if choice == 1:
                    self.to_hunting()
                elif choice == 2:
                    self.to_fake_fights()
                elif choice == 3:
                    self.to_relax()
                elif choice == 4:
                    pass
                else:
                    raise ValueError
                is_choice_correct = True
            except ValueError:
                print("Ви мали обрати номер від 1 до 4!")
    def live(self, day_index):
        self.pick_active()
        self.calculate_values()
        if self.end_day(day_index) == False:
            return False
        return True
    def end_day(self, day_index):
        massage = f"Закінчився {day_index + 1} день"
        print(f"\n{massage:=^45}")

        dead_wolves = []
        for wolf in self.wolfs:
            if wolf.end_day() == False:
                dead_wolves.append(wolf)
        for wolf in dead_wolves:
            self.remove_wolf(wolf)

        if len(self.wolfs) <= 2 or self.average_mood <= -12:
            print("Нажаль, зграя розвалилася")
            return False

        print("Параметри вовків:")
        print(f"Середнє здоров'є вовків: {round(self.average_health, 2)}")
        print(f"Середній настрій вовків: {round(self.average_mood, 2)}")
        print(f"Середня ситість вовків: {round(self.average_satiety, 2)}")
        print(f"Середня сила вовків: {round(self.average_strength, 2)}")
        print(f"Кількість вовків у зграї: {len(self.wolfs)}")
        print(f"Кількість ворожих зграй: {self.number_enemy_flocks}")
        return True

flock = Flock()
for day_index in range(61):
    if flock.live(day_index) == False:
        break