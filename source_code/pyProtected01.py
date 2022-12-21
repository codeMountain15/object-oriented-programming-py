# pyProtected01.py

# parent class
class Animal:
	
	# protected attributes (data members)
	_name = None
	_weight = None
	_height = None
	
	# constructor
	def __init__(self, name, weight, height):
		self._name = name
		self._weight = weight
		self._height = height
	
	# protected member function
	def _showInfo(self):

		# access protected attributes (data members)
		print("Name: ", self._name)
		print("Weight: ", self._weight)
		print("Height: ", self._height)


# inheritance
class Gourouni(Animal):

	# constructor
	def __init__(self, name, weight, height):
				Animal.__init__(self, name, weight, height)
		
	# public member function
	def displayDetails(self):
		# accessing inherited member method
		self._showInfo(self)
				

obj01 = Gourouni("Dj", 60, 0.5)

# call public member functions
obj01._showInfo()
