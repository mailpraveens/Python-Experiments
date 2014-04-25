def find_sum_of_fibonacci():
	sum = 0
	a , b = 0, 1
	while True:
		a , b = b , a + b
		if b > 4000000:
			break
		if b % 2 == 0:
			sum += b

	print sum


def main():
	find_sum_of_fibonacci()

if __name__ == '__main__':
	main()