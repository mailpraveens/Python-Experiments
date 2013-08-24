import sys

def is_happy(x): 
	#split the number and add the squares until the sum reaches 1
	#break if you find a number already visited
	already_got_num = []
	while not x == 1 and x not in already_got_num:
		already_got_num.append(x)
		x = sum([int(digit)**2 for digit in str(x)]) #Convert number to digits and add the squares

	return 1 if x == 1 else 0


test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    test = test.strip('\n')
    print is_happy(test)

test_cases.close()
