'''
		1
	2		3
  4   5   6    7


 should print 1,2,4,5,6,7,3,1


'''

class BinaryTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None
	def printBoundaryOfaTree(self):
		self.preOrderLeftOnly()
		self.inOrderLeafOnly()
		self.postOrderRightOnly()

	def isLeafNode(self,x):
		return (x != None and x.left == None and x.right == None)

	def preOrderLeftOnly(self):
		if (self!=None and not(self.isLeafNode(self))):
			print (self.value )
		if self.left != None :
			self.left.preOrderLeftOnly()

	def inOrderLeafOnly(self):
		if (self ==  None):
			 return
		if (self.left!=None):
			self.left.inOrderLeafOnly()
		if (self.left == None and self.right == None):
			print (self.value )
		if (self.right != None):
			self.right.inOrderLeafOnly()

	def postOrderRightOnly(self):	
		if self.right != None :
			self.right.postOrderRightOnly()
		if (self!=None and not(self.isLeafNode(self))):
			print(self.value )


def constructTree():
	tree = BinaryTree(1)
	tree.left = BinaryTree(2)
	tree.right = BinaryTree(3)
	tree.left.left = BinaryTree(4)
	tree.left.right = BinaryTree(5)
	tree.right.left = BinaryTree(6)
	tree.right.right = BinaryTree(7)		
	tree.printBoundaryOfaTree()

def main():
	constructTree() 
 
if __name__=='__main__':
  main()
