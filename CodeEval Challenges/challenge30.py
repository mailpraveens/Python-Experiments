import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	list1, list2 = test.split(';') # 1,2,3,4 ; 2,3,4,5 --> 1,2,3,4,5
	print ','.join(list(set(list1.split(',')) & set(list2.split(','))))

test_cases.close()