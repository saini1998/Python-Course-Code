from abc import ABC, abstractmethod
from collections import namedtuple


class Point:
    default_colour = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x} , {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x+another.x, self.y + another.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_colour = "yellow"
point = Point(10, 20)
print(isinstance(point, Point))
print(point.default_colour)
print(Point.default_colour)
point.draw()

another = Point(3, 4)
print(another.default_colour)
another.draw()
print(point + another)
print(point == another)
one_more = Point.zero()
one_more.draw()

# Google python 3 magic methods
print(point)


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud["python"]  # = 10
len(cloud)
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud._TagCloud__tags)


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can not be negative")
        self.__price = value


product = Product(10)
print(product.price)


class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()  # method overriding
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):

        print("walk")


class Fish(Animal):
    def walk(self):
        print("walk")


m = Mammal()
m.eat()
print(m.age)

print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
print(issubclass(Mammal, object))

# replacing or extending a method defined in the base class
print(m.weight)

# multilevel inheritance
# increases complexity so avoid it as much as possible


# multiple inheritance

class employee:
    def greet(self):
        print("employee says hi")


class person:
    def greet(self):
        print("person says hi")


class manager(person, employee):
    pass


Manager = manager()
Manager.greet()

# use multiple inheritance when abstract classes are there

# A good example of inheritance


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")


# Abstract base class

# from abc import ABC,abstractmethod
# can not instantiate abstract class

stream = FileStream()
stream.read()
stream.open()
print(stream.opened)


# Polymorphism NOTE  many forms
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("textbox")


class DropDownList(UIControl):
    def draw(self):
        print("Dropdown list")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()

draw([textbox, ddl])

# NOTE DUCK TYPING
# class TextBox():
#     def draw(self):
#         print("textbox")


# class DropDownList():
#     def draw(self):
#         print("Dropdown list")


# def draw(controls):
#     for control in controls:
#         control.draw() # NOTE if it walks like a duck, quaks like a duck. it is duck


# ddl = DropDownList()
# textbox = TextBox()

# draw([textbox, ddl])

# Extending Built-In Types

class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("append called")
        super().append(object)


list = TrackableList()
list.append("1")

# DATA CLASSES


class PointTwo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# NOTE instead of this
# from collections import namedtuple
p21 = PointTwo(1, 2)
p22 = PointTwo(1, 2)

print(p21 == p22)

PointThree = namedtuple("PointThree", ["x", "y"])
p31 = PointThree(x=1, y=2)
p32 = PointThree(x=1, y=2)
print(p31 == p32)
# to set a value of attribute p31 = PointThree(x=10,y=2)
