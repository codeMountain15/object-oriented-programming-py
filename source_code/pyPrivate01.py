# pyPrivate01.py

class Animal:
	
	# private attributes (data members)
	__name = None
	__weight = None
	__height = None
	
	# constructor
	def __init__(self, name, weight, height):
		self.__name = name
		self.__weight = weight
		self.__height = height
	
	# public member function
	def showInfo(self):

		# access private attributes (data members)
		print("Name: ", self.__name)
		print("Weight: ", self.__weight)
		print("Height: ", self.__height)
				

obj01 = Animal("Dj", 60, 0.5)

# call public member function
obj01.showInfo()
