import sys
def remove_duplicates(n):
	output = []
	for elem in n.strip().split(','):
		if elem not in output:
			output.append(elem)
			
	return ','.join(output)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	print remove_duplicates(test)

test_cases.close()