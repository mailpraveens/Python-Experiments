def calculate(n):
    if n == 1:
        return 1
	if n % 2 == 0:
		n = n/2
	else:
		n = 3 * n + 1;
	return 1 + calculate(n)


		n = int(raw_input("Enter the number:"))
		print calculate(n)
