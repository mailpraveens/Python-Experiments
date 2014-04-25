def gcd(a,b):
	"""Returns the gcd of two numbers a and b """
	while b:
		a , b = b , a % b

	return a

def lcm(a,b):
	return a * b / gcd(a, b)


def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)


def main():
	print lcmm(*range(1,20))

if __name__ == '__main__':
	main()