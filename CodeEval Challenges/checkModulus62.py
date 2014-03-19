import sys
def get_modulus(n,m):
	quotient = n / m;
	return n - (quotient * m) 

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if not test == '\n':
		#Get the two numbers, and call the method
		a,b = [int(elem) for elem in test.split(',')]
		print get_modulus(a,b)

test_cases.close()