# encoding:utf-8

class Employee():
    """ 员工类 """

    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def give_raise(self,salary = 5000):
        self.salary = salary