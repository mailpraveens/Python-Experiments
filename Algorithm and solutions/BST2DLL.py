from CounterClockwiseBinaryTree import BinaryTree

def bst2dll(tree,head=None):
	if tree is not None:
		head = bst2dll(tree.left,head)
		if(head is None):
			head = tree
			head.left = tree
		else:
			tree.left = head.left
			head.left = tree
			tree.left.right = tree
		right = tree.right
		tree.right = head

		head = bst2dll(right,head)
		return head
	else:
		return head		


def main():
	tree = BinaryTree(1)
	tree.left = BinaryTree(2)
	tree.right = BinaryTree(3)
	tree.left.left = BinaryTree(4)
	tree.left.right = BinaryTree(5)
	tree.right.left = BinaryTree(6)
	tree.right.right = BinaryTree(7)		
	bst2dll(tree,None)
	head = tree
	while (head.left and head.left != tree):
		print(head.value)
		head = head.left



if __name__ == '__main__':
	main()