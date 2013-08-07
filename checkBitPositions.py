import sys

def check_bit_positions(n, p1, p2):
    """Checks if the first two digits of n match p1 and p2."""
    binary = '{0:b}'.format(n)
    if list(binary)[-p1] == list(binary)[-p2]:
    	print "true"
    else:
    	print "false"

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if not test == '\n':
		#Get the two numbers, and call the method
		n,a,b = [int(elem) for elem in test.split(',')]
		check_bit_positions(n,a,b)

test_cases.close()