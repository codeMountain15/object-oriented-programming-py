# pySuper01.py
#

class Dog():
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("gav gav gav gav")

class europeanDog(Dog):
  # implements parent-class
  # init() function
  def __init__(self, name, category):
    self.category = category
    super().__init__(name)

  # implements parent-class
  # sound() function
  def sound(self):
      super().sound();

  def who_am_I(self):
      print("I am ", self.name, ", a ", self.category, " dog!")


obj01 = europeanDog("Kitsos", "Gekas")
obj01.sound()
obj01.who_am_I()
