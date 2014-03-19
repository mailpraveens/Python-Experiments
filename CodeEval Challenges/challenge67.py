
#This program converts the input hex number to its decimal equivalent.
import sys

#Read the file from terminal
test_cases = open(sys.argv[1],'r')

#Remove white spaces and empty lines and make a list for all the test in test_cases
tests = [test.strip() for test in test_cases if not test == '\n']

#now convert each of the tests into decimal using the int(num,base)

for test in tests:
	print str(int(test,16))

test_cases.close()