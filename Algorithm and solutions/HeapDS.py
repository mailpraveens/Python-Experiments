import math

def leftChild(idx):
	return 2*idx+1
def rightChild(idx):
	return 2*idx+2

def build_heap(items):
    count = len(items)
    for i in range(int(math.floor(count/2)) - 1, -1, -1):
		heapify(items,i)
#max heap construction
def heapify(items,idx):
	left = leftChild(idx)
	right = rightChild(idx)
	largest = -1
	if(left < len(items) and items[left] > items[idx]):
		largest = left
	else:
		largest = idx

	if(right < len(items) and items[right] > items[largest]):
		largest = right

	if(largest != idx):
		temp = items[idx]
		items[idx] = items[largest]
		items[largest] = temp
		heapify(items,largest)


def main():
	items = [5,3,17,10,84,19,6,22,9]
	build_heap(items)
	print(items)

if __name__ == '__main__':
	main()