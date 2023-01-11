from abc import ABC, abstractmethod


# The Factory method
class Shape(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError

    @staticmethod
    def factory(shape_type):
        if shape_type == 'square':
            obj = Square(100, 100)
        elif shape_type == 'circle':
            obj = Circle(100, 100)
        else:
            raise ValueError(f"We don't have shape with type {shape_type}")
        return obj


class Square(Shape):

    def draw(self):
        print(f'Square was drown at {self.x} - {self.y}')


class Circle(Shape):

    def draw(self):
        print(f'Circle was drown at {self.x} - {self.y}')


# The Abstract factory
class AbstractShape(ABC):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def make_object(self):
        pass


class SquareFactory(AbstractShape):

    def make_object(self):
        print(f'Square object was made {self.x} - {self.y}')
        return Square(self.x, self.y)


class CircleFactory(AbstractShape):

    def make_object(self):
        print(f'Circle object was made {self.x} - {self.y}')
        return Circle(self.x, self.y)


def draw_new_shape(factory):
    drawable = factory.make_object()
    drawable.draw()


def prepare_all_objects():
    square = SquareFactory(300, 300)
    circle = CircleFactory(300, 300)
    for factory in (square, circle):
        draw_new_shape(factory)


if __name__ == "__main__":
    # The Factory method
    for shape in ('square', 'circle'):
        drawable = Shape.factory(shape)
        drawable.draw()
    # The Abstract factory
    prepare_all_objects()

