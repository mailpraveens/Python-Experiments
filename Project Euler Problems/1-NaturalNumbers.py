def find_sum_of_multiples():
	sum = 0
	for i in range(1000):
		if (i % 3 == 0):	
			sum += i
		elif (i % 5 == 0):
			sum += i
	return sum


def main():
	sum = find_sum_of_multiples();
	print sum

if __name__ == '__main__':
	main()