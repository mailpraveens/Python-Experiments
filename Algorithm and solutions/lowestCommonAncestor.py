from CounterClockwiseBinaryTree import BinaryTree

def findLCA(node,value1,value2):
	if(node == None):
		return None
	#move to right if values are greater
	if(node.value < value1 and node.value < value2):
		return findLCA(node.right,value1, value2)
	#move to left if values are smaller
	if(node.value > value1 and node.value > value2):
		return findLCA(node.left,value1, value2)
	# Whereever it diverges, return the node as its the LCA
	return node


def main():
	tree = BinaryTree(5)
	tree.left = BinaryTree(2)
	tree.right = BinaryTree(18)
	tree.left.left = BinaryTree(1)
	tree.left.right = BinaryTree(3)
	tree.right.left = BinaryTree(15)
	tree.right.right = BinaryTree(20)		
	lca = findLCA(tree,15,20)
	print(lca.value)



if __name__ == '__main__':
	main()