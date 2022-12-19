# pyInheritance03.py
# __init__() override

class Bird:
   name = "Bifis"
   type = "I said Bird!"
   
   def __init__(self, name, type):
       self.name = name
       self.type = type

   def printInfo(self):
    print("I am ", self.name, " and I\'m a ", self.type)

class Chicken(Bird):
    def __init__(self, name):
       self.name = name
    
    # access the inherited attribute: type
    def info(self):
       print(self.type)

obj01 = Chicken("Koko")
obj01.info();
