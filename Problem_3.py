from numpy.linalg import matrix_power
import numpy as np

num = 600851475143

def is_prime(n):
	for f in range(2, int(n**0.5)):
		if n % f == 0:
			return False
	return True

def solution():
	current_num = int(num**0.5)
	while not num % current_num == 0 or not is_prime(current_num):
		current_num -= 1
	return current_num

print solution()
