#! usr/bin/env python

# Derek Bean
# ME 599
# lab 5
# 2/14/2017

import numpy as np

class Circle:


	def __init__(self, radius):
		self.radius = radius
	

	def __mul__(self, other):
		return self.radius * other


	def __pow__(self, other):
		return self.radius ** other


	def diameter(self):
		return self.radius*2


	def area(self):
		return np.pi*self.radius**2


	def circumference(self):
		return 2*np.pi*self.radius


if __name__ == '__main__':
	# Area check
	radius = 1
	A = Circle(radius)

	if A.radius != radius:
		print 'The wrong radius was returned'
	if A.diameter() != 2* radius:
		print 'The wrong diameter was returned'
	if A.area() != np.pi*radius**2:
		print 'The wrong area was returned'
	if A.circumference() != 2*np.pi*radius:
		print 'The wrong circumference was returned'

