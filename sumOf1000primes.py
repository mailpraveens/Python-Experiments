import sys
import math

def is_prime(num):
	for j in range(2,int(math.sqrt(num))+1):
		if (num % j) == 0:
			return False
	return True

i = 0
j=2
sum = 0
while (i < 1000):
	if is_prime(j):
		sum += j
		i += 1	
	j += 1

print sum