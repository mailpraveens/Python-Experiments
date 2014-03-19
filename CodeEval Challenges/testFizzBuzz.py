import sys

def test_fizz_buzz(a,b,n):
	output = [];

	for i in range(1,n+1):
		isFizz = (i % a) == 0;
		isBuzz = (i % b ) == 0;

		if isBuzz and isFizz:
			output.append('FB')
		elif isFizz:
			output.append('F')
		elif isBuzz:
			output.append('B')
		else:
			output.append(str(i))

	return ' '.join(output)

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
    if not test == '\n':
    #Split the input into the three params needed by casting to int
        a, b, n = [int(elem) for elem in test.split()]
        print test_fizz_buzz(a, b, n)

test_cases.close()