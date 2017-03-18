from math import floor
from random import randint
from math import log

# The priority queue is built using the MinHeap class. 
# The number of elements in the heap is stored here along 
# with arrays of the symbols and their frequencies
class MinHeap:
	def __init__(self, length):
# size is intialized to 1 so the parent/left/right operations work correctly. 
# If initialized to 0 they do not produce the right calculations.
# A placeholder of -1 is used for the 0th position of the arrays 
# while infinity placeholders are used for the remaining positions. 
		self.size = 1 
		self.S = [-1] + [float("inf")]*length
		self.f = [-1] + [float("inf")]*length
		self.ops = 0

# These calculations are used for the parent/child 
# relationships in the S/f arrays
	def parent(self, i):
		return int(floor(i/2))

	def left(self, i):
		return 2*i

	def right(self, i):
		return 2*i + 1

# The min heap requires swapping elements a few times, 
# so this code has been abstracted away into a swap function
	def swap(self, i, j):
		temp = self.f[i]
		self.f[i] = self.f[j]
		self.f[j] = temp
		temp = self.S[i]
		self.S[i] = self.S[j]
		self.S[j] = temp

# insert adds the new node at the last positon of the S/f arrays.  
# The node is then bubbled up through the tree structure 
# with the cleanup function
	def insert(self, Si, fi):
		self.S[self.size] = Si
		self.f[self.size] = fi
		self.cleanup(self.size)
		self.size = self.size + 1

# cleanup checks if node is smaller than its parent. 
# If so, they are swapped to preserve the min priority queue
	def cleanup(self, i):
		pi = self.parent(i)
# swaps last node with its parent until in correct position
		while self.f[i] < self.f[pi]:
			self.ops += 1
			self.swap(pi, i)
			i = pi

# deletemin extracts the root value of S/f.  
# It then moves the last node of the array into the root position and sets 
# that position to use the infinity placeholders for consistency.
# cleandown is called which moves the new root down to its correct place 
# in the tree structure. If the new root is larger than its smallest child, 
# then they need to be swapped.  This is repeated until the new root is 
# in the correct position.
	def deletemin(self):
# extract minimum node at root
		m = (self.S[1], self.f[1])
# swap last node into root position
		self.S[1] = self.S[self.size-1]
		self.f[1] = self.f[self.size-1]
# reset -1 placeholders to indicate no value there
		self.S[self.size-1] = float("inf")
		self.f[self.size-1] = float("inf")
# reduce size of heap
		self.size = self.size - 1
		def cleandown(i):
			self.ops += 1
			root = self.f[i]
			left = self.f[self.left(i)]
			right = self.f[self.right(i)]
			minimum = min(left, right)
			if left == float("inf") and right == float("inf"):
				minimum = -1
			elif minimum == self.f[self.left(i)]:
				minimum = self.left(i)
			else:
				minimum = self.right(i)
			if root > self.f[minimum] and self.f[minimum] != -1:
				# swap with the smaller of its children
				self.swap(i, minimum)
				cleandown(minimum)
		cleandown(1)
		return m