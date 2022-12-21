# pyInheritance06.py
# add a method to object

class Dog():
    def __init__(self, name, category):
        self.name = name
        self.category = category

class strayDog(Dog):
  pass

# create an object
obj01 = strayDog("Mourgos", "affenshire")

# create a method
def reveal_id(self):
    print("I\'m ", self.name, " and I\'m a ", self.category)

# add/bound the method to the object
obj01.reveal_id = reveal_id.__get__(obj01)

# and it works!!
obj01.reveal_id()
