# pyClasses03.py
# delete object attribute/property

class Student:
   def __init__(self, name, department):
       self.name = name
       self.department = department

obj01 = Student("Manousos", "Informatics")
print(obj01.name)

del obj01.name
print(obj01.name) # error!
