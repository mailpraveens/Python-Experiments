import sys
    
test_cases = open(sys.argv[1], 'r')
total = 0
for test in test_cases:
	total += int(test.strip())

print str(total)

test_cases.close()