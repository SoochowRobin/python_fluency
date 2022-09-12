# This class is used to create a 2-d vector and this vector could also extend to n-dimensional vectors 

# note that the none of them is directly called within the class or in the typical usage of the class illustrated by the doctests.
# the python interpreter is the only frequent calller of the most special methods.
import math

class Vector:

	def __init__(self, x=0, y=0) -> None:
		self.x = x
		self.y = y
	
	# __repr__ special method would return representaiton for this instance, if there is not 
	# return <Vector object at 0x10e...>
	def __repr__(self) -> str:
		return f'Vector({self.x}, {self.y})'
	
	def __abs__(self):
		return math.hypot(self.x, self.y)
	
	def __bool__(self):
		return bool(abs(self))


	def __add__(self, other):
		x = self.x + other.x
		y = self.y + other.y
		return Vector(x, y)
	
	def __mul__(self, scalar):
		return Vector(self.x * scalar, self.y * scalar)
	


# test here
v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1+v2)

# print absolute value
print(abs(v1))

print(v1)