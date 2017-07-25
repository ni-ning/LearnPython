#!/usr/bin/env python3
# -*-coding:utf-8 -*-
# __author__:Jonathan
# email:nining1314@gmail.com

class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('eat...')

    def talk(self):
        print('%s is talk...' % self.name)

class People(Animal):

    def __init__(self, name, age, sex, education):
        Animal.__init__(self, name, age, sex)    # 子类调用父类的方法
        self.education = education

    def talk(self):
        print('%s say hello' % self.name)

class Pig(Animal):
    pass

class Dog(Animal):
    pass

peo1 = People('Linda', 18, 'female', '本科')  # People.__init__()，现在People里找__init__()，找不到再到父类Animal里面找
pig1 = Pig('Tom', 20, 'male')
dog1 = Dog('旺财', 4, 'male')

print(isinstance(peo1, People))
print(isinstance(pig1, Pig))
print(isinstance(dog1, Dog))

print(isinstance(peo1, Animal))
print(isinstance(pig1, Animal))
print(isinstance(dog1, Animal))

# 继承反映的是一种什么时什么的关系

# 组合也可以解决代码冗余问题，但是组合反映的是一种什么有什么的关系

class Date:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def tell(self):
        print('%s-%s-%s' % (self.year, self.mon, self.day))


class Teacher(People):
    def __init__(self, name, age, sex, salary, year, mon, day):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.birth = Date(year, mon, day)  # 老师有生日


class Student(People):
    def __init__(self, name, age, sex, year, mon, day):
        self.name = name
        self.age = age
        self.sex = sex
        self.birth = Date(year, mon, day)

t = Teacher('Linda', 18, 'female', 3000, 2011, 11, 11)
t.birth.tell() # 2011-11-11

s = Student('Tom', 20, 'male', 2011, 11, 11)



