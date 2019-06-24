from math import sqrt
from time import time, localtime, sleep
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        pass


class Dog(Pet):
    def make_voice(self):
        print("wan wan")


class Cat(Pet):
    def make_voice(self):
        print("meow")




class Person(object):
    __slots__ = ("_name", "_age", "_gender", "_xx")
    def __init__(self, name, age, gender, xx):
        self._name = name
        self._age = age
        self._gender = gender
        self._xx = xx
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    @property
    def gender(self):
        return self._gender
    def play(self):
        if(self._age > 18):
            print("%s is playing galgame" % (self._name))
        else:
            print("%s is playing meow" % (self._name))


class Triangle(object):
    __slots__ = ("_a", "_b", "_c")
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    @staticmethod
    def isValid(a, b, c):
        return a + b > c and a + c > b and b + c > a
    def perimeter(self):
        return self._a + self._b + self._c
    def area(self):
        half_perimeter = self.perimeter() / 2
        return sqrt(half_perimeter * (half_perimeter - self._a) * (half_perimeter - self._b) * (half_perimeter - self._c))


class Clock(object):
    __slots__ = ("_hour", "_min", "_sec")
    def __init__(self, hour, min, sec):
        self._hour = hour
        self._min = min
        self._sec = sec
    def run(self):
        self._sec += 1
        if self._sec >= 60:
            self._sec = 0
            self._min += 1
            if self._min >= 60:
                self._min = 0
                self._hour += 1
                if self._hour >= 24:
                    self._hour = 0
    def show(self):
        print("%02d-%02d-%02d" % (self._hour, self._min, self._sec))
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

d = Dog("haha")
d.make_voice()

c = Cat("meow")
c.make_voice()

if Triangle.isValid(3, 4, 5):
    tri = Triangle(3, 4, 5)
    print(tri.perimeter())
    print(tri.area())

miao = Person("zhu", 18, "female", "xx")
miao.play()
miao.age = 20
miao.play()
print(miao.age)
clock = Clock.now()
while True:
    clock.show()
    sleep(1)
    clock.run()


