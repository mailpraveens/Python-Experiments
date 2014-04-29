import math
def sum_of_digits():
	sum = 0
	num =  2**1000
	print str(num) 
	for s in str(num):
		sum += int(s)
	
	print sum


def main():
	sum_of_digits()

if __name__ == '__main__':
	main()