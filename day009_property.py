class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):
        self._age = age
    def play(self):
        if(self._age > 18):
            print("%s is playing galgame" % (self._name))
        else:
            print("%s is playing meow" % (self._name))

miao = Person("zhu", 18)
miao.play()
miao.age = 20
miao.play()
print(miao.age)
