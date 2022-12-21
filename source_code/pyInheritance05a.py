# pyInheritance05a.py
#

class Dog():
    def __init__(self, name, category):
        self.name = name
        self.category = category

class strayDog(Dog):
  pass

obj01 = strayDog("Mourgos", "unknown")

# add a new attribute to obj01
#obj01.weight = 10
setattr(obj01, "weight", 15)

print(obj01.name)
print(obj01.category)
print(obj01.weight)
