from abc import ABCMeta, abstractmethod



class Employee(object, metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @abstractmethod
    def get_salary(self):
        pass


class Programmer(Employee):
    def __init__(self, name):
        super().__init__(name)
        self._work_hour = 0
    @property
    def work_hour(self):
        return self._work_hour
    @work_hour.setter
    def work_hour(self, hour):
        self._work_hour = hour
    def get_salary(self):
        return self.work_hour * 50


class Manager(Employee):
    def get_salary(self):
        return 15000


class Sale(Employee):
    def __init__(self, name):
        super().__init__(name)
        self._sales = 0
    @property
    def sales(self):
        return self._sales
    @sales.setter
    def sales(self, sale):
        self._sales = sale
    def get_salary(self):
        return 10000 + self.sales * 0.05


emps = [
    Programmer("A"),
    Manager("B"),
    Sale("C")
]

for emp in emps:
    if isinstance(emp, Programmer):
        emp.work_hour = 240
    elif isinstance(emp, Sale):
        emp.sales = 1000000
    print("%s:%d" % (emp.name, emp.get_salary()))


