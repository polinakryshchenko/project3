import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print('Studying...')
        self.progress += 0.12
        self.gladness -= 5

    def to_sleep(self):
        print('Zzz!')
        self.gladness += 3

    def to_chill(self):
        print('Chilling...')
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print('Cast out!')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression!')
            self.alive = False
        elif self.progress > 5:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print('gladness', self.gladness)
        print('progress', self.progress)

    def live(self, day):
        print(f"Day N {day} of {self.name}'s life")
        dice = random.randint(1, 3)
        if dice == 1:
            self.to_study()
        elif dice == 2:
            self.to_sleep()
        elif dice == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


nick = Student(name='Nick')

for day in range(365):
    if not nick.alive:
        break
    nick.live(day)
