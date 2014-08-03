import sys

#Store the already computed values for fast recovery
alreadyComputedValues = {0:0}
def getBytelandianMax(n):
	if n in alreadyComputedValues:
		return alreadyComputedValues[n]
	bytemax = getBytelandianMax(int(n//2)) + getBytelandianMax(int(n//3)) + getBytelandianMax(int(n//4));
	alreadyComputedValues[n] = max(n, bytemax);
	return alreadyComputedValues[n]




#to get input from command line - Woof that was an effort
if __name__ == "__main__":
    while True:
        try:
            num = int(input())
            sys.stdout.write("%d\n" % getBytelandianMax(int(num)))
        except:
            break