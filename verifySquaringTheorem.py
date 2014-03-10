#http://www.quora.com/Whats-a-math-trick-that-is-not-very-well-known/answers/4234574
import sys
def verifySquaringTheorem(n):
	for i in range(25,n):
		nSquaredSupposed = (( i - 25 ) * 100) + pow(i-50,2)
		actualSquare = pow(i,2);
		if nSquaredSupposed == actualSquare:
			print ("Pass for n = " + str(i) + " with value " + str(nSquaredSupposed))
		else:
			print("Fail for n = " + str(i) + "with value " + str(nSquaredSupposed) + "and actualSquare value = " + str(actualSquare))
		
	return


def main():	
	verifySquaringTheorem(1000)

if __name__ == '__main__':
	main()