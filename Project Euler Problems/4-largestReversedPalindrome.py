def check_if_palindrome(string):
	rev = string[::-1] #reverse the string
	return rev == string #returns the bool


def check_for_reverse_palindrome():
	longest_reverse_palindrome = 0
	for i in reversed(range(100,1000,1)):
		for j in reversed(range(i, 1000, 1)):
			prod = i * j
			if check_if_palindrome(str(prod)) and longest_reverse_palindrome < prod:
				longest_reverse_palindrome = prod

	print longest_reverse_palindrome

def main():
	check_for_reverse_palindrome()

if __name__ == '__main__':
	main()