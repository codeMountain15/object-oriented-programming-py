# pyInheritance04.py
# 

class Bird:
   name = "Bifis"
   type = "I said Bird!"
   
   def __init__(self, name, type):
       self.name = name
       self.type = type
       print("This is Bird init")

   
class Chicken(Bird):
    def __init__(self, name, type):
       # call parent class __init__()
       Bird.__init__(self, name, type)
       print("This is Chicken init")


obj01 = Chicken("Koko", "Chicken")
