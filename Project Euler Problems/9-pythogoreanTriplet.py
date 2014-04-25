def find_special_pythagorean_triplet():
	for a in range(1,1000):
		for b in range(a+1, 1000):
			c = 1000 - b - a
			if c*c == a*a + b*b:
				print a*b*c




def main():
	find_special_pythagorean_triplet()

if __name__ == '__main__':
	main()