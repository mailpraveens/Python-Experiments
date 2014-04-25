def sum_of_squares(n):
	sum = 0;
	for i in range(1,n+1):
		print i
		sum += i*i

	return sum

def sum_of_n_numbers(n):
	return ((n * (n+1))/2)


def main():
	print sum_of_squares(100) - (sum_of_n_numbers(100)**2)

if __name__ == '__main__':
	main()