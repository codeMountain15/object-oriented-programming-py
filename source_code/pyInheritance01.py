# pyInheritance01.py
# 

class Bird:
   def __init__(self, name, type):
       self.name = name
       self.type = type

   def printInfo(self):
    print("I am ", self.name, " and I\'m a ", self.type)

class Chicken(Bird):
    pass

obj01 = Chicken("Koko", "chicken")
obj01.printInfo()
print(obj01)
