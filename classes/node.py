# The Node class is used to build the tree for use in creating the codebook
class Node:
	def __init__(self, key, left, leftval, right, rightval):
		self.key = key
		self.left = left
		self.leftval = leftval
		self.right = right
		self.rightval = rightval