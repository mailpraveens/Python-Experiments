def largest_prime_factor(num):
	n = num
	i = 2

	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1

	return n

def main():
	print largest_prime_factor(600851475143)


if __name__ == '__main__':
	main()