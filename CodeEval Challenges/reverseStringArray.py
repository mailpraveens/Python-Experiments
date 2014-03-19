import sys
test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test == '\n':
    #Split by space, reverse and print with a space
    	print ' '.join(reversed(test.split()))

test_cases.close()