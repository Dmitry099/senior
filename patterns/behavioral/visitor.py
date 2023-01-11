import random
from abc import ABC, abstractmethod


class Visitable:
    def accept(self, visitor):
        visitor.visit(self)


class CompositeVisitable(Visitable):
    def __init__(self, iterable):
        self.iterable = iterable

    def accept(self, visitor):
        for element in self.iterable:
            element.accept(visitor)
        visitor.visit(self)


class AbstractVisitor(ABC):

    @abstractmethod
    def visit(self, element):
        pass


class Light(Visitable):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    @staticmethod
    def get_status():
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.status != -1

    def boot_up(self):
        self.status = 0


class LightStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home):
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        if self.person_1_home:
            if self.person_2_home:
                element.status = 1
            else:
                element.status = 0
        elif self.person_2_home:
            element.status = 1
        else:
            element.status = 0


class DoorLock(Visitable):
    def __init__(self, name):
        self.name = name
        self.status = self.get_status()

    @staticmethod
    def get_status():
        return random.choice(range(-1, 2))

    def is_online(self):
        return self.status != -1

    def boot_up(self):
        pass


class DoorLockStatusUpdateVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home):
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        if self.person_1_home:
            element.status = 0
        elif self.person_2_home:
            element.status = 1
        else:
            element.status = 1


class CompositeVisitor(AbstractVisitor):
    def __init__(self, person_1_home, person_2_home):
        self.person_1_home = person_1_home
        self.person_2_home = person_2_home

    def visit(self, element):
        try:
            visitor = globals()[
                "{}StatusUpdateVisitor".format(element.__class__.__name__)
            ]
        except KeyError:
            print(
                "Visitor for {} not found". format(
                    element.__class__.__name__
                )
            )
        else:
            v = visitor(self.person_1_home, self.person_2_home)
            v.visit(element)


class MyHomeSystem(CompositeVisitable):
    pass


def main():
    my_home_system = MyHomeSystem([
        Light("Bedroom Light"),
        DoorLock("Fron Door Lock")
    ])
    visitor = CompositeVisitor(True, True)
    my_home_system.accept(visitor)
    print(sorted([str(x.status) for x in my_home_system.iterable]))


if __name__ == '__main__':
    main()