from classes.node import Node
from classes.minheap import MinHeap

def string2freq(x):
	Sf = {} # create dictionary of values
	for c in x:
		if c == " ":
			c = "sp"
# character is not in Sf so add it with frequency 1
		if c not in Sf: 
			Sf[c] = 1
		else:
# character is in Sf so increment frequency by 1
			Sf[c] = Sf[c] + 1 
# separate out dictionary structure into two lists 
# and sort in lexicographic order
	Sfp = []
	for key in sorted(Sf.iterkeys()):
		Sfp.append([key, Sf[key]])
	Sfp  = zip(*Sfp)
	return Sfp

# build out the codebook using a heap, H.
def codebook(H):
	codebook = {} # use dictionary for codebook
	encode = ""
	def traverse(node, encode):
# symbol nodes don't have left and right children. 
# If the node is not a symbol, it must have left and right children.
		if isinstance(node, Node):
			traverse(node.left, "1" + encode)
			traverse(node.right, "0" + encode)
		else:
			H.ops += 1
			codebook[node] = encode
	traverse(H.S[1], encode)
	return codebook

def huffmanEncode(S, f, length):
	H = MinHeap(length) # create priority queue using a MinHeap
	n = len(f)
	for i in range(0, n): # insert all the values into the Heap
		H.ops += 1
		H.insert(S[i], f[i])
	for k in range(n, 2*n-1):
		H.ops += 1
		i = H.deletemin() # get min value
		j = H.deletemin() # get min value
		s = i[1] + j[1] # find their frequency sum
# create a node with the information of two min values and their sum
		z = Node(s, i[0], i[1], j[0], j[1]) 
		H.insert(z, s) # insert new node into the queue.
# run codebook on the heap to generate the optimal encodings
	return H.ops, codebook(H)

# converts a string x into an optimal huffman encoding using codebook T
def encodeString(x, T):
	y = ""
	for i in range(0, len(x)):
		c = x[i]
		if c == " ":
			c = "sp"
		y = y + T[c]
	return y

def main():
	print
	x = "the road not taken by robert frost two roads diverged in a yellow wood, and sorry i could not travel both and be one traveler, long i stood and looked down one as far as i could to where it bent in the undergrowth; then took the other, as just as fair, and having perhaps the better claim, because it was grassy and wanted wear; though as for that the passing there had worn them really about the same, and both that morning equally lay in leaves no step had trodden black. oh, i kept the first for another day! yet knowing how way leads on to way, i doubted if i should ever come back. i shall be telling this with a sigh somewhere ages and ages hence: two roads diverged in a wood, and i- i took the one less traveled by, and that has made all the difference."
	S,f = string2freq(x)


	ops, codebook = huffmanEncode(S, f, 100)
	y = encodeString(x, codebook)
	print "Encoding:"
	print "-----------------------------------"
	print(y)
	print
	print "Codebook:"
	print "-----------------------------------"
	print codebook
	print

if __name__ == "__main__":
	main()