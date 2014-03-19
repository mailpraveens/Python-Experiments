import sys

def fib(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)



test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if not test == '\n':
		print fib(int(test.strip()))
        
test_cases.close()