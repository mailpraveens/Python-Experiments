def calculateLevenSteninDistance(a,b):
    if not a: return len(b)
    if not b: return len(a)
    return min(calculateLevenSteninDistance(a[1:], b[1:])+(a[0] != b[0]), calculateLevenSteninDistance(a[1:], b)+1, calculateLevenSteninDistance(a, b[1:])+1)



def main():
	print(calculateLevenSteninDistance("abcda","cccda"))


if __name__ == '__main__':
	main()