import sys
#add the number to itself untill it becomes greater that the given number
def find_multiple(a,b):
	while(b < a):
		b += b
	return b

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if not test == '\n':
		#Get the two numbers, and call the method
		a,b = [int(elem) for elem in test.split(',')]
		print find_multiple(a,b)

test_cases.close()
