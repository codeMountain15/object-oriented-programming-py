# pyClasses05.py
#

class Dog():
    def __init__(self, name, category):
        self.name = name
        self.category = category

class strayDog(Dog):
  pass


obj01 = strayDog("Mourgos", "unknown")
obj01.weight = 10

print(obj01.name)
print(obj01.category)
print(obj01.weight)
