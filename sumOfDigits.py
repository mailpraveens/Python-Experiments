import sys

def sum_of_digits(num):
    if num < 10:
        return num
    else:
        return num % 10 + sum_of_digits(num/10) 

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	if not test == '\n':
        print sum_of_digits(int(test.strip()))
        
test_cases.close()	