import sys
import math

def is_prime(num):
	for j in range(2,int(math.sqrt(num))+1):
		if (num % j) == 0:
			return False
	return True

def is_palindrome(num):
	return str(num) == str(num)[::-1]

for i in reversed(range(1,1000)):
	if is_prime(i):
		if is_palindrome(i):
			print i
			break