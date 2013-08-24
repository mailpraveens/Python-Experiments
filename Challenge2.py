#Program to find the n largest lines in a file
import operator
import sys

#Read the file from terminal
test_cases = open(sys_argv[1],'r')

#Remove white spaces and empty lines and make a list for all the test in test_cases
tests = [test_cases.strip() for test in test_cases if not test == '\n']

#The first element in the file is the number of lines to print
num = int(tests.pop(0))


#read every line and find the length, Create a dictionary with key as the line length
dict_for_lines = dict(zip([len(line) for line in tests], tests))


#Using the sorted function sort the lines
sorted_lines = sorted(dict_for_lines.iteritems(), key = operator.itemgetter(0), reverse = TRUE)

print '\n'.join([line for length, line in sorted_lines[:num]])

test_cases.close()