import random
from abc import ABCMeta, abstractmethod
from copy import deepcopy


class Unit(metaclass=ABCMeta):

    def __init__(self, life, attack, defence, level):
        self.life = life
        self.attack = attack
        self.defence = defence
        self.level = level
        self.name = None

    def clone(self):
        new_instance = deepcopy(self)
        new_instance.generate_name()
        return new_instance

    @abstractmethod
    def generate_name(self):
        self.name = random.randint(0, 100000)


class Knight(Unit):

    def generate_name(self):
        self.name = f'Knight_{random.randint(0, 100000)}'


class Archer(Unit):

    def generate_name(self):
        self.name = f'Archer_{random.randint(0, 100000)}'


class Barracks(object):
    units = {
        'knight': Knight(100, 10, 15, 1),
        'archer': Archer(80, 15, 8, 2)
    }

    def generate_units(self, type):
        return self.units[type].clone()


if __name__ == '__main__':
    b = Barracks()
    knight_1, knight_2 = b.generate_units('knight'), b.generate_units('knight')
    archer_1, archer_2 = b.generate_units('archer'), b.generate_units('archer')
    print(knight_1.name, knight_2.name, archer_1.name, archer_2.name)

