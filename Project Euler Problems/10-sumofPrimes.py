
def is_prime(n):
	if n % 2 == 0: return False
	for i in xrange(3, int(n**0.5), 2):
		if n % i == 0:
			return False
	return True


def main():
	i = 3 
	sum = 2
	while(i < 2000000):
		if is_prime(i):
			sum += i
		i += 1
	print sum

if __name__ == '__main__':
	main()

