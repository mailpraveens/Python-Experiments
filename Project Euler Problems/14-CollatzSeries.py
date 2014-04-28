def find_longest_collatz_series():
	maxnum = 1000000 #one million is the max from which the longest collatz is to be found
	computed = {} #list to save the already computed values
	sequence = 1
	sequenceLength = 0
	startingnumber  = 0
	for i in range(0,maxnum):
		computed[i] = -1;

	computed[1] = 1
	for i in range(2, maxnum):
		sequence = i
		k = 0
		while sequence != 1 and sequence >=i:
			k += 1
			if sequence % 2 == 0:
				sequence = sequence / 2
			else:
				sequence = (3 * sequence) + 1
		computed [i] = k + computed[sequence]
		if computed[i] > sequenceLength:
			sequenceLength = computed[i]
			startingnumber = i
	print startingnumber 
	print computed[startingnumber]


def main():
	find_longest_collatz_series()


if __name__ == '__main__':
	main()