# pyInheritance02.py
# __init__() override

class Bird:
   def __init__(self, name, type):
       self.name = name
       self.type = type
       print("This is Bird init")

   def printInfo(self):
    print("I am ", self.name, " and I\'m a ", self.type)

class Chicken(Bird):
    # child __init__() overrides
    # parent __init__()
    def __init__(self, name, type):
       self.name = name
       self.type = type
       print("This is Chicken init")

obj01 = Chicken("Koko", "chicken")
