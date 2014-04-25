#find the nth prime number
#Gives the wrong answer
def nth_prime(n):
	k = 0
	i = 2
	while True:
		if is_prime(i):
			k += 1
			if k == n:
				break
		i += 1

	return i

def is_prime(n):
	if n % 2 == 0: return False
	for i in xrange(3, int(n**0.5), 2):
		if n % i == 0:
			return False

	return True

def main():
	print nth_prime(10001)

if __name__ == '__main__':
	main()